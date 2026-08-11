#!/usr/bin/env python3
"""Pipeline local e auditável para download, transcrição e tradução da entrevista.

Rede é proibida por padrão. As únicas etapas capazes de usar rede exigem uma
opção explícita: ``--allow-network`` ou ``--allow-model-download``.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
import json
import os
import platform
import re
import shlex
import shutil
import subprocess
import sys
import wave
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable
from uuid import uuid4


SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent
CONFIG_PATH = PROJECT_DIR / "config.json"
RAW_DIR = PROJECT_DIR / "data" / "raw"
PROCESSED_DIR = PROJECT_DIR / "data" / "processed"
OUTPUT_DIR = PROJECT_DIR / "outputs"
METADATA_DIR = PROJECT_DIR / "metadata"
LOG_DIR = PROJECT_DIR / "logs"
SEGMENTS_PATH = METADATA_DIR / "segmentos_whisper.json"
TRANSLATIONS_PATH = METADATA_DIR / "segmentos_traducao.json"
SPEAKERS_PATH = METADATA_DIR / "speakers.tsv"
WAV_PATH = PROCESSED_DIR / "entrevista_16k_mono.wav"

MEDIA_SUFFIXES = {".aac", ".flac", ".m4a", ".mp3", ".mp4", ".ogg", ".opus", ".wav", ".webm"}
ALLOWED_NAMED_SPEAKERS = {"Host", "Angela", "Gabriel", "Alejandro"}


def load_config() -> dict[str, Any]:
    return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))


def utc_stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")


def iso_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def human_size(size: int) -> str:
    value = float(size)
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if value < 1024 or unit == "TB":
            return f"{value:.1f} {unit}"
        value /= 1024
    raise AssertionError("unreachable")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def atomic_write_text(path: Path, text: str, *, overwrite: bool = False) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not overwrite:
        raise FileExistsError(f"Recusa de sobrescrita: {path}")
    temporary = path.with_name(f".{path.name}.tmp-{uuid4().hex}")
    temporary.write_text(text, encoding="utf-8")
    os.replace(temporary, path)


def atomic_write_json(path: Path, payload: Any, *, overwrite: bool = False) -> None:
    atomic_write_text(
        path,
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        overwrite=overwrite,
    )


def record_command(command: list[str]) -> None:
    METADATA_DIR.mkdir(parents=True, exist_ok=True)
    line = f"{iso_now()}\t{shlex.join(command)}\n"
    with (METADATA_DIR / "executed_commands.log").open("a", encoding="utf-8") as stream:
        stream.write(line)


def run_logged(command: list[str], label: str) -> subprocess.CompletedProcess[str]:
    record_command(command)
    result = subprocess.run(command, text=True, capture_output=True, check=False)
    log_text = (
        f"command: {shlex.join(command)}\n"
        f"returncode: {result.returncode}\n\n"
        f"[stdout]\n{result.stdout}\n\n[stderr]\n{result.stderr}\n"
    )
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    atomic_write_text(LOG_DIR / f"{label}_{utc_stamp()}.log", log_text)
    return result


def executable(name: str) -> str | None:
    local = PROJECT_DIR / ".venv" / "bin" / name
    if local.is_file() and os.access(local, os.X_OK):
        return str(local)
    return shutil.which(name)


def module_available(name: str) -> bool:
    return importlib.util.find_spec(name) is not None


def model_cache_root() -> Path:
    explicit = os.environ.get("HF_HUB_CACHE")
    if explicit:
        return Path(explicit).expanduser()
    hf_home = Path(os.environ.get("HF_HOME", "~/.cache/huggingface")).expanduser()
    return hf_home / "hub"


def cached_snapshot(model_id: str) -> Path | None:
    model_dir = model_cache_root() / f"models--{model_id.replace('/', '--')}"
    snapshots = model_dir / "snapshots"
    if not snapshots.is_dir():
        return None
    ref = model_dir / "refs" / "main"
    candidates: list[Path] = []
    if ref.is_file():
        resolved = snapshots / ref.read_text(encoding="utf-8").strip()
        if resolved.is_dir():
            candidates.append(resolved)
    candidates.extend(sorted((p for p in snapshots.iterdir() if p.is_dir()), reverse=True))
    for candidate in candidates:
        config_ok = (candidate / "config.json").is_file()
        weights_ok = any(
            (candidate / filename).is_file()
            for filename in (
                "model.safetensors",
                "model.safetensors.index.json",
                "pytorch_model.bin",
                "pytorch_model.bin.index.json",
            )
        )
        if config_ok and weights_ok:
            return candidate
    return None


def tool_version(command: list[str]) -> str | None:
    try:
        result = subprocess.run(command, text=True, capture_output=True, timeout=20, check=False)
    except (OSError, subprocess.TimeoutExpired):
        return None
    combined = (result.stdout or result.stderr).strip().splitlines()
    return combined[0] if combined else None


def command_preflight(args: argparse.Namespace) -> int:
    config = load_config()
    whisper_snapshot = cached_snapshot(config["whisper_model_id"])
    translation_snapshot = cached_snapshot(config["translation_model_id"])
    tools = {
        name: {"path": executable(name), "version": None}
        for name in ("yt-dlp", "ffmpeg", "ffprobe", "uv")
    }
    if tools["yt-dlp"]["path"]:
        tools["yt-dlp"]["version"] = tool_version([tools["yt-dlp"]["path"], "--version"])
    if tools["ffmpeg"]["path"]:
        tools["ffmpeg"]["version"] = tool_version([tools["ffmpeg"]["path"], "-version"])

    modules = {
        name: module_available(name)
        for name in ("numpy", "torch", "transformers", "sentencepiece", "ctranslate2", "faster_whisper")
    }
    converted = PROJECT_DIR / config["converted_whisper_model_dir"]
    payload = {
        "checked_at": iso_now(),
        "network_used": False,
        "python": {"executable": sys.executable, "version": platform.python_version()},
        "platform": {"system": platform.system(), "release": platform.release(), "machine": platform.machine()},
        "tools": tools,
        "modules": modules,
        "models": {
            "whisper_source_cache": str(whisper_snapshot) if whisper_snapshot else None,
            "whisper_converted": str(converted) if (converted / "model.bin").is_file() else None,
            "translation_cache": str(translation_snapshot) if translation_snapshot else None,
        },
    }
    output = METADATA_DIR / f"preflight_{utc_stamp()}.json"
    atomic_write_json(output, payload)
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    print(f"\nInventário salvo em {output}")

    required_tools_ok = all(tools[name]["path"] for name in ("yt-dlp", "ffmpeg", "ffprobe"))
    required_modules_ok = all(modules[name] for name in ("numpy", "torch", "transformers", "sentencepiece"))
    whisper_ok = whisper_snapshot is not None
    if args.strict and not (required_tools_ok and required_modules_ok and whisper_ok):
        print("Preflight estrito: FALHA", file=sys.stderr)
        return 1
    print("Preflight: PASS" if required_tools_ok and required_modules_ok and whisper_ok else "Preflight: PENDÊNCIAS")
    return 0


def raw_media_files() -> list[Path]:
    return sorted(
        p
        for p in RAW_DIR.iterdir()
        if p.is_file() and p.suffix.lower() in MEDIA_SUFFIXES and not p.name.startswith(".")
    ) if RAW_DIR.is_dir() else []


def choose_raw_media() -> Path:
    files = raw_media_files()
    if not files:
        raise FileNotFoundError("Nenhum áudio bruto encontrado em data/raw.")
    youtube = [path for path in files if path.name.startswith("youtube_")]
    return youtube[0] if youtube else files[0]


def download_source(url: str, source_id: str) -> tuple[bool, Path | None, str]:
    yt_dlp = executable("yt-dlp")
    if not yt_dlp:
        raise RuntimeError("yt-dlp não encontrado.")
    output_template = str(RAW_DIR / f"{source_id}.%(ext)s")
    command = [
        yt_dlp,
        "--no-playlist",
        "--no-overwrites",
        "--continue",
        "--retries", "10",
        "--fragment-retries", "10",
        "--socket-timeout", "30",
        "--write-info-json",
        "--format", "bestaudio",
        "--output", output_template,
        url,
    ]
    result = run_logged(command, f"download_{source_id}")
    matches = sorted(path for path in raw_media_files() if path.name.startswith(f"{source_id}."))
    media = matches[0] if matches else None
    return result.returncode == 0 and media is not None, media, result.stderr[-4000:]


def command_download(args: argparse.Namespace) -> int:
    if not args.allow_network:
        print("Rede bloqueada. Use --allow-network somente após autorização.", file=sys.stderr)
        return 2
    existing = raw_media_files()
    if existing:
        print(f"Áudio bruto já existe; nenhuma rede usada: {choose_raw_media()}")
        return 0

    RAW_DIR.mkdir(parents=True, exist_ok=True)
    config = load_config()
    attempts: list[dict[str, Any]] = []
    sources = [
        (config["primary_url"], "youtube_n34CIw3gk1k", "youtube_primary"),
        (config["fallback_url"], "x_2086845184785203468", "x_fallback"),
    ]
    selected: Path | None = None
    selected_source: str | None = None
    for url, filename_id, source_name in sources:
        print(f"Tentando {source_name}...")
        ok, media, error_tail = download_source(url, filename_id)
        attempts.append({"source": source_name, "url": url, "ok": ok, "error_tail": error_tail})
        if ok and media:
            selected = media
            selected_source = source_name
            break
        print(f"{source_name} falhou; preservando logs e tentando a alternativa segura.", file=sys.stderr)

    payload = {
        "executed_at": iso_now(),
        "selected_source": selected_source,
        "selected_file": str(selected) if selected else None,
        "attempts": attempts,
    }
    atomic_write_json(METADATA_DIR / "source_run.json", payload)
    if not selected:
        print("As duas fontes falharam. Consulte os logs em logs/.", file=sys.stderr)
        return 1
    print(f"Áudio salvo sem playlist em {selected}")
    return 0


def probe_media(path: Path) -> dict[str, Any]:
    ffprobe = executable("ffprobe")
    if not ffprobe:
        raise RuntimeError("ffprobe não encontrado.")
    command = [
        ffprobe,
        "-v", "error",
        "-show_streams",
        "-show_format",
        "-of", "json",
        str(path),
    ]
    record_command(command)
    result = subprocess.run(command, text=True, capture_output=True, check=False)
    if result.returncode != 0:
        raise RuntimeError(f"ffprobe falhou: {result.stderr.strip()}")
    return json.loads(result.stdout)


def media_duration(probe: dict[str, Any]) -> float:
    try:
        return float(probe["format"]["duration"])
    except (KeyError, TypeError, ValueError) as exc:
        raise ValueError("Duração do áudio não encontrada pelo ffprobe.") from exc


def command_normalize(_: argparse.Namespace) -> int:
    if WAV_PATH.exists():
        print(f"Áudio normalizado já existe; nada foi sobrescrito: {WAV_PATH}")
        return 0
    source = choose_raw_media()
    probe = probe_media(source)
    stream_types = [stream.get("codec_type") for stream in probe.get("streams", [])]
    if "audio" not in stream_types:
        raise RuntimeError("O arquivo bruto não contém fluxo de áudio.")
    if "video" in stream_types:
        raise RuntimeError("O arquivo bruto contém vídeo; a regra de baixar somente áudio foi violada.")
    duration = media_duration(probe)
    expected = float(load_config()["expected_duration_minutes"]) * 60
    if duration < 600 or duration > 10800:
        raise RuntimeError(f"Duração incompatível com uma entrevista: {duration:.1f} segundos.")
    if abs(duration - expected) > 600:
        print(f"AVISO: duração {duration / 60:.1f} min difere da expectativa de {expected / 60:.1f} min.")

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    temporary = WAV_PATH.with_name(f".{WAV_PATH.name}.tmp-{uuid4().hex}.wav")
    ffmpeg = executable("ffmpeg")
    if not ffmpeg:
        raise RuntimeError("ffmpeg não encontrado.")
    command = [
        ffmpeg, "-nostdin", "-hide_banner", "-loglevel", "warning", "-n",
        "-i", str(source), "-vn", "-ac", "1", "-ar", "16000",
        "-c:a", "pcm_s16le", str(temporary),
    ]
    result = run_logged(command, "normalize_audio")
    if result.returncode != 0 or not temporary.is_file():
        raise RuntimeError("ffmpeg falhou; o arquivo bruto foi preservado. Consulte logs/.")
    os.replace(temporary, WAV_PATH)
    atomic_write_json(
        METADATA_DIR / "audio_probe.json",
        {"probed_at": iso_now(), "source": str(source), "duration_seconds": duration, "ffprobe": probe},
    )
    print(f"Áudio normalizado salvo em {WAV_PATH}")
    return 0


def command_convert_model(_: argparse.Namespace) -> int:
    config = load_config()
    output_dir = PROJECT_DIR / config["converted_whisper_model_dir"]
    if (output_dir / "model.bin").is_file():
        print(f"Modelo CTranslate2 já existe: {output_dir}")
        return 0
    if output_dir.exists() and any(output_dir.iterdir()):
        raise RuntimeError(f"Conversão parcial encontrada; preservada para diagnóstico: {output_dir}")
    snapshot = cached_snapshot(config["whisper_model_id"])
    if not snapshot:
        raise RuntimeError("Modelo Whisper-base ausente do cache; conversão local impossível.")
    converter = executable("ct2-transformers-converter")
    if not converter:
        raise RuntimeError("ct2-transformers-converter ausente; instale o ambiente local autorizado.")
    output_dir.parent.mkdir(parents=True, exist_ok=True)
    command = [
        converter,
        "--model", str(snapshot),
        "--output_dir", str(output_dir),
        "--copy_files", "tokenizer.json", "preprocessor_config.json",
        "--quantization", "int8",
    ]
    result = run_logged(command, "convert_whisper_model")
    if result.returncode != 0 or not (output_dir / "model.bin").is_file():
        raise RuntimeError("Conversão para CTranslate2 falhou; o cache-base foi preservado.")
    print(f"Modelo convertido localmente em {output_dir}")
    return 0


def read_pcm_wav(path: Path) -> tuple[Any, int, float]:
    import numpy as np

    with wave.open(str(path), "rb") as stream:
        channels = stream.getnchannels()
        sample_width = stream.getsampwidth()
        sample_rate = stream.getframerate()
        frames = stream.getnframes()
        data = stream.readframes(frames)
    if (channels, sample_width, sample_rate) != (1, 2, 16000):
        raise ValueError(
            f"WAV incompatível: channels={channels}, width={sample_width}, rate={sample_rate}."
        )
    waveform = np.frombuffer(data, dtype="<i2").astype("float32") / 32768.0
    return waveform, sample_rate, frames / sample_rate


def normalize_segment(start: Any, end: Any, text: Any, duration: float) -> dict[str, Any] | None:
    cleaned = re.sub(r"\s+", " ", str(text or "")).strip()
    if not cleaned:
        return None
    start_value = max(0.0, float(start or 0.0))
    end_value = duration if end is None else min(duration, float(end))
    if end_value <= start_value:
        return None
    return {"start": round(start_value, 3), "end": round(end_value, 3), "text": cleaned}


def transcribe_faster_whisper(config: dict[str, Any]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    from faster_whisper import WhisperModel

    model_dir = PROJECT_DIR / config["converted_whisper_model_dir"]
    if not (model_dir / "model.bin").is_file():
        raise RuntimeError("Modelo convertido do faster-whisper não encontrado.")
    _, _, duration = read_pcm_wav(WAV_PATH)
    model = WhisperModel(
        str(model_dir),
        device="cpu",
        compute_type="int8",
        cpu_threads=max(1, os.cpu_count() or 4),
        num_workers=1,
    )
    iterator, info = model.transcribe(
        str(WAV_PATH),
        language="en",
        task="transcribe",
        beam_size=5,
        temperature=0,
        condition_on_previous_text=True,
        vad_filter=True,
        vad_parameters={"min_silence_duration_ms": 500},
        word_timestamps=False,
    )
    segments: list[dict[str, Any]] = []
    for segment in iterator:
        item = normalize_segment(segment.start, segment.end, segment.text, duration)
        if item:
            item["avg_logprob"] = getattr(segment, "avg_logprob", None)
            item["no_speech_prob"] = getattr(segment, "no_speech_prob", None)
            segments.append(item)
    metadata = {
        "backend": "faster-whisper",
        "model": config["whisper_model_id"],
        "converted_model": str(model_dir),
        "compute_type": "int8",
        "device": "cpu",
        "detected_language": getattr(info, "language", None),
        "language_probability": getattr(info, "language_probability", None),
        "audio_duration_seconds": duration,
    }
    return segments, metadata


def transcribe_transformers(
    config: dict[str, Any], *, allow_model_download: bool, device_request: str
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    import numpy as np
    import torch
    from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline

    snapshot = cached_snapshot(config["whisper_model_id"])
    if snapshot:
        model_source = str(snapshot)
        local_only = True
    elif allow_model_download:
        model_source = config["whisper_model_id"]
        local_only = False
    else:
        raise RuntimeError("Modelo Whisper ausente do cache e download de modelo não autorizado.")

    if device_request == "auto":
        device = "mps" if torch.backends.mps.is_available() else "cpu"
    else:
        device = device_request
    if device == "mps" and not torch.backends.mps.is_available():
        raise RuntimeError("Dispositivo MPS solicitado, mas indisponível.")
    dtype = torch.float16 if device == "mps" else torch.float32
    waveform, sample_rate, duration = read_pcm_wav(WAV_PATH)

    processor = AutoProcessor.from_pretrained(model_source, local_files_only=local_only)
    model = AutoModelForSpeechSeq2Seq.from_pretrained(
        model_source,
        local_files_only=local_only,
        use_safetensors=True,
        dtype=dtype,
    )
    model.to(device)
    model.eval()
    asr = pipeline(
        "automatic-speech-recognition",
        model=model,
        tokenizer=processor.tokenizer,
        feature_extractor=processor.feature_extractor,
        chunk_length_s=30,
        stride_length_s=(5, 2),
        return_timestamps=True,
        dtype=dtype,
        device=device,
    )
    with torch.inference_mode():
        result = asr(
            {"raw": np.asarray(waveform), "sampling_rate": sample_rate},
            generate_kwargs={"language": "en", "task": "transcribe"},
        )
    raw_chunks = result.get("chunks") or [{"timestamp": (0.0, duration), "text": result.get("text", "")}]
    segments: list[dict[str, Any]] = []
    for chunk in raw_chunks:
        start, end = chunk.get("timestamp") or (0.0, duration)
        item = normalize_segment(start, end, chunk.get("text"), duration)
        if item:
            segments.append(item)
    metadata = {
        "backend": "transformers",
        "model": config["whisper_model_id"],
        "model_source": model_source,
        "dtype": str(dtype),
        "device": device,
        "detected_language": "en",
        "audio_duration_seconds": duration,
    }
    return segments, metadata


def check_segments(segments: list[dict[str, Any]]) -> list[str]:
    problems: list[str] = []
    previous_start = -1.0
    for index, segment in enumerate(segments, start=1):
        try:
            start = float(segment["start"])
            end = float(segment["end"])
            text = str(segment["text"]).strip()
        except (KeyError, TypeError, ValueError):
            problems.append(f"segmento {index}: estrutura inválida")
            continue
        if start < 0 or end <= start:
            problems.append(f"segmento {index}: intervalo inválido {start}–{end}")
        if start < previous_start:
            problems.append(f"segmento {index}: timestamps fora de ordem")
        if not text:
            problems.append(f"segmento {index}: texto vazio")
        previous_start = start
    if not segments:
        problems.append("nenhum segmento")
    return problems


def format_srt_time(seconds: float) -> str:
    milliseconds = int(round(max(0.0, seconds) * 1000))
    hours, remainder = divmod(milliseconds, 3_600_000)
    minutes, remainder = divmod(remainder, 60_000)
    secs, millis = divmod(remainder, 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"


def format_clock(seconds: float) -> str:
    whole = int(max(0.0, seconds))
    hours, remainder = divmod(whole, 3600)
    minutes, secs = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"


def load_speaker_annotations(path: Path = SPEAKERS_PATH) -> list[dict[str, Any]]:
    if not path.is_file():
        return []
    lines = [line for line in path.read_text(encoding="utf-8").splitlines() if not line.startswith("#")]
    if not lines:
        return []
    rows: list[dict[str, Any]] = []
    for row in csv.DictReader(lines, delimiter="\t"):
        label = (row.get("label") or "").strip()
        confidence = (row.get("confidence") or "").strip().lower()
        evidence = (row.get("evidence") or "").strip()
        if not label:
            continue
        generic = re.fullmatch(r"Speaker [1-9][0-9]*", label) is not None
        named = label in ALLOWED_NAMED_SPEAKERS
        if not (generic or named):
            raise ValueError(f"Rótulo de falante não permitido: {label}")
        if named and (confidence != "high" or not evidence):
            raise ValueError(f"O nome {label} exige confidence=high e evidência explícita.")
        start = float(row["start_seconds"])
        end = float(row["end_seconds"])
        if start < 0 or end <= start:
            raise ValueError(f"Intervalo inválido no mapa de falantes: {start}–{end}")
        rows.append({"start": start, "end": end, "label": label, "confidence": confidence, "evidence": evidence})
    return sorted(rows, key=lambda item: (item["start"], item["end"]))


def speaker_for_interval(start: float, end: float, annotations: list[dict[str, Any]]) -> str:
    midpoint = (start + end) / 2
    for item in annotations:
        if item["start"] <= midpoint < item["end"]:
            return str(item["label"])
    return "Speaker não identificado"


def render_english_outputs(payload: dict[str, Any], *, overwrite: bool) -> None:
    config = load_config()
    segments = payload["segments"]
    annotations = load_speaker_annotations()
    txt = "\n".join(segment["text"] for segment in segments).strip() + "\n"
    srt_parts = []
    for index, segment in enumerate(segments, start=1):
        srt_parts.append(
            f"{index}\n{format_srt_time(segment['start'])} --> {format_srt_time(segment['end'])}\n"
            f"{segment['text']}\n"
        )
    srt = "\n".join(srt_parts).rstrip() + "\n"

    block_seconds = int(config["markdown_block_minutes"]) * 60
    grouped: dict[int, list[dict[str, Any]]] = {}
    for segment in segments:
        grouped.setdefault(int(float(segment["start"]) // block_seconds), []).append(segment)
    lines = [
        "# Transcrição integral em inglês",
        "",
        f"- Fonte preferencial: {config['primary_url']}",
        f"- Modelo: `{payload['metadata']['model']}` via `{payload['metadata']['backend']}`",
        "- Regra editorial: transcrição integral; sem resumo e sem preenchimento de lacunas.",
        "",
    ]
    for block_index in sorted(grouped):
        block_start = block_index * block_seconds
        block_end = block_start + block_seconds
        lines.extend([f"## {format_clock(block_start)}–{format_clock(block_end)}", ""])
        for segment in grouped[block_index]:
            speaker = speaker_for_interval(segment["start"], segment["end"], annotations)
            lines.append(
                f"[{format_clock(segment['start'])}–{format_clock(segment['end'])}] "
                f"**{speaker}:** {segment['text']}"
            )
            lines.append("")

    atomic_write_text(OUTPUT_DIR / "transcricao_ingles.txt", txt, overwrite=overwrite)
    atomic_write_text(OUTPUT_DIR / "transcricao_ingles.srt", srt, overwrite=overwrite)
    atomic_write_text(OUTPUT_DIR / "transcricao_ingles.md", "\n".join(lines).rstrip() + "\n", overwrite=overwrite)


def translation_chunks(segments: list[dict[str, Any]], block_seconds: int, max_chars: int) -> list[dict[str, Any]]:
    del block_seconds
    chunks: list[dict[str, Any]] = []
    for segment in segments:
        text = str(segment["text"]).strip()
        if len(text) > max_chars:
            raise ValueError(
                f"Segmento de {len(text)} caracteres excede o limite seguro de tradução ({max_chars})."
            )
        chunks.append({"start": segment["start"], "end": segment["end"], "source_text": text})
    return chunks


def command_transcribe(args: argparse.Namespace) -> int:
    if SEGMENTS_PATH.exists():
        print(f"Segmentos já existem; nada foi sobrescrito: {SEGMENTS_PATH}")
        return 0
    if not WAV_PATH.is_file():
        raise FileNotFoundError(f"Áudio normalizado ausente: {WAV_PATH}")
    config = load_config()
    requested_backend = args.backend
    backend = requested_backend
    converted = PROJECT_DIR / config["converted_whisper_model_dir"] / "model.bin"
    if backend == "auto":
        backend = "faster-whisper" if converted.is_file() and module_available("faster_whisper") else "transformers"
    print(f"Backend de transcrição selecionado: {backend}")
    if backend == "faster-whisper":
        try:
            segments, metadata = transcribe_faster_whisper(config)
        except Exception as exc:
            if requested_backend != "auto":
                raise
            print(
                f"AVISO: faster-whisper falhou ({exc}); tentando transformers com o mesmo modelo local.",
                file=sys.stderr,
            )
            segments, metadata = transcribe_transformers(
                config,
                allow_model_download=args.allow_model_download,
                device_request=args.device,
            )
    else:
        segments, metadata = transcribe_transformers(
            config,
            allow_model_download=args.allow_model_download,
            device_request=args.device,
        )
    problems = check_segments(segments)
    if problems:
        raise RuntimeError("Segmentos inválidos: " + "; ".join(problems[:10]))
    payload = {"created_at": iso_now(), "metadata": metadata, "segments": segments}
    atomic_write_json(SEGMENTS_PATH, payload)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    render_english_outputs(payload, overwrite=False)
    print(f"Transcrição salva em {SEGMENTS_PATH} e outputs/transcricao_ingles.*")
    return 0


def command_translate(args: argparse.Namespace) -> int:
    if TRANSLATIONS_PATH.exists():
        print(f"Tradução já existe; nada foi sobrescrito: {TRANSLATIONS_PATH}")
        return 0
    if not SEGMENTS_PATH.is_file():
        raise FileNotFoundError("Execute a transcrição antes da tradução.")
    import torch
    from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

    config = load_config()
    source_payload = json.loads(SEGMENTS_PATH.read_text(encoding="utf-8"))
    block_seconds = int(config["markdown_block_minutes"]) * 60
    chunks = translation_chunks(
        source_payload["segments"],
        block_seconds,
        int(config["translation_chunk_max_chars"]),
    )
    snapshot = cached_snapshot(config["translation_model_id"])
    if snapshot:
        model_source = str(snapshot)
        local_only = True
    elif args.allow_model_download:
        model_source = config["translation_model_id"]
        local_only = False
    else:
        print("Modelo NLLB ausente e download bloqueado. Use --allow-model-download após autorização.", file=sys.stderr)
        return 2

    device = args.device
    if device == "auto":
        device = "mps" if torch.backends.mps.is_available() else "cpu"
    if device == "mps" and not torch.backends.mps.is_available():
        raise RuntimeError("Dispositivo MPS solicitado, mas indisponível.")
    dtype = torch.float16 if device == "mps" else torch.float32
    tokenizer = AutoTokenizer.from_pretrained(
        model_source,
        src_lang="eng_Latn",
        local_files_only=local_only,
    )
    model = AutoModelForSeq2SeqLM.from_pretrained(
        model_source,
        local_files_only=local_only,
        use_safetensors=True,
        dtype=dtype,
    )
    model.to(device)
    model.eval()
    target_token = tokenizer.convert_tokens_to_ids("por_Latn")

    partial = TRANSLATIONS_PATH.with_suffix(".partial.json")
    translated: list[dict[str, Any]] = []
    if partial.is_file():
        partial_payload = json.loads(partial.read_text(encoding="utf-8"))
        translated = partial_payload.get("chunks", [])
        for index, old in enumerate(translated):
            if index >= len(chunks) or old.get("source_text") != chunks[index]["source_text"]:
                raise RuntimeError("Checkpoint de tradução incompatível; preservado para diagnóstico.")
        print(f"Retomando tradução no bloco {len(translated) + 1} de {len(chunks)}.")

    batch_size = int(config["translation_batch_size"])
    for batch_start in range(len(translated), len(chunks), batch_size):
        batch = chunks[batch_start:batch_start + batch_size]
        lengths = [len(tokenizer(item["source_text"], add_special_tokens=True)["input_ids"]) for item in batch]
        if any(length > 512 for length in lengths):
            raise RuntimeError("Um segmento excede 512 tokens; tradução interrompida antes de truncar conteúdo.")
        encoded = tokenizer(
            [item["source_text"] for item in batch],
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=512,
        ).to(device)
        input_tokens = max(lengths)
        with torch.inference_mode():
            generated = model.generate(
                **encoded,
                forced_bos_token_id=target_token,
                num_beams=4,
                do_sample=False,
                max_new_tokens=min(640, max(80, input_tokens * 3)),
            )
        target_texts = [text.strip() for text in tokenizer.batch_decode(generated, skip_special_tokens=True)]
        if len(target_texts) != len(batch) or any(not text for text in target_texts):
            raise RuntimeError(f"Tradução vazia ou desalinhada no lote iniciado em {batch_start + 1}.")
        translated.extend(
            {**source, "target_text": target}
            for source, target in zip(batch, target_texts, strict=True)
        )
        checkpoint = {
            "created_at": iso_now(),
            "model": config["translation_model_id"],
            "source_language": "eng_Latn",
            "target_language": "por_Latn",
            "chunks": translated,
        }
        atomic_write_json(partial, checkpoint, overwrite=True)
        print(f"Traduzidos segmentos {batch_start + 1}–{batch_start + len(batch)}/{len(chunks)}")

    if TRANSLATIONS_PATH.exists():
        raise FileExistsError(f"Recusa de sobrescrita: {TRANSLATIONS_PATH}")
    os.replace(partial, TRANSLATIONS_PATH)
    render_portuguese_output(
        json.loads(TRANSLATIONS_PATH.read_text(encoding="utf-8")),
        overwrite=False,
    )
    print(f"Tradução local salva em {TRANSLATIONS_PATH}")
    return 0


def render_portuguese_output(payload: dict[str, Any], *, overwrite: bool) -> None:
    config = load_config()
    annotations = load_speaker_annotations()
    block_seconds = int(config["markdown_block_minutes"]) * 60
    grouped: dict[int, list[dict[str, Any]]] = {}
    for chunk in payload["chunks"]:
        grouped.setdefault(int(float(chunk["start"]) // block_seconds), []).append(chunk)
    lines = [
        "# Tradução integral para o português",
        "",
        f"- Fonte preferencial: {config['primary_url']}",
        f"- Modelo local de tradução: `{payload['model']}`",
        "- Regra editorial: tradução integral; sem resumo e sem preenchimento de lacunas.",
        "",
    ]
    for block_index in sorted(grouped):
        block_start = block_index * block_seconds
        block_end = block_start + block_seconds
        lines.extend([f"## {format_clock(block_start)}–{format_clock(block_end)}", ""])
        for chunk in grouped[block_index]:
            speaker = speaker_for_interval(chunk["start"], chunk["end"], annotations)
            lines.append(
                f"[{format_clock(chunk['start'])}–{format_clock(chunk['end'])}] "
                f"**{speaker}:** {chunk['target_text']}"
            )
            lines.append("")
    atomic_write_text(OUTPUT_DIR / "traducao_portugues.md", "\n".join(lines).rstrip() + "\n", overwrite=overwrite)


def command_render(args: argparse.Namespace) -> int:
    if not SEGMENTS_PATH.is_file():
        raise FileNotFoundError("Segmentos Whisper ausentes.")
    payload = json.loads(SEGMENTS_PATH.read_text(encoding="utf-8"))
    render_english_outputs(payload, overwrite=args.replace_generated)
    if TRANSLATIONS_PATH.is_file():
        translated = json.loads(TRANSLATIONS_PATH.read_text(encoding="utf-8"))
        render_portuguese_output(translated, overwrite=args.replace_generated)
    else:
        print("Tradução ainda ausente; apenas os arquivos em inglês foram renderizados.")
    return 0


def final_artifact_paths() -> list[Path]:
    paths = [
        OUTPUT_DIR / "transcricao_ingles.txt",
        OUTPUT_DIR / "transcricao_ingles.srt",
        OUTPUT_DIR / "transcricao_ingles.md",
        OUTPUT_DIR / "traducao_portugues.md",
        SEGMENTS_PATH,
        TRANSLATIONS_PATH,
        WAV_PATH,
    ]
    paths.extend(raw_media_files())
    return paths


def command_validate(_: argparse.Namespace) -> int:
    required = final_artifact_paths()[:7]
    missing = [path for path in required if not path.is_file() or path.stat().st_size == 0]
    if missing:
        for path in missing:
            print(f"FALHA: ausente ou vazio: {path.relative_to(PROJECT_DIR)}", file=sys.stderr)
        return 1

    segments_payload = json.loads(SEGMENTS_PATH.read_text(encoding="utf-8"))
    segments = segments_payload.get("segments", [])
    problems = check_segments(segments)
    if problems:
        for problem in problems:
            print(f"FALHA: {problem}", file=sys.stderr)
        return 1
    duration = float(segments_payload["metadata"].get("audio_duration_seconds", 0))
    if not (1500 <= duration <= 3000):
        print(f"FALHA: duração {duration:.1f}s fora da faixa plausível de 25–50 minutos.", file=sys.stderr)
        return 1
    srt = (OUTPUT_DIR / "transcricao_ingles.srt").read_text(encoding="utf-8")
    srt_entries = len(re.findall(r"(?m)^\d+$", srt))
    if srt_entries != len(segments):
        print(f"FALHA: SRT tem {srt_entries} entradas para {len(segments)} segmentos.", file=sys.stderr)
        return 1
    translated = json.loads(TRANSLATIONS_PATH.read_text(encoding="utf-8"))
    if not translated.get("chunks") or any(not item.get("target_text", "").strip() for item in translated["chunks"]):
        print("FALHA: tradução vazia ou incompleta.", file=sys.stderr)
        return 1
    if len(translated["chunks"]) != len(segments):
        print(
            f"FALHA: tradução tem {len(translated['chunks'])} unidades para {len(segments)} segmentos.",
            file=sys.stderr,
        )
        return 1
    load_speaker_annotations()

    artifacts = []
    checksum_lines = []
    for path in sorted(set(final_artifact_paths())):
        if not path.is_file() or path.name == ".gitkeep":
            continue
        digest = sha256(path)
        relative = path.relative_to(PROJECT_DIR)
        artifacts.append(
            {"path": str(relative), "bytes": path.stat().st_size, "human_size": human_size(path.stat().st_size), "sha256": digest}
        )
        checksum_lines.append(f"{digest}  {relative}")
    atomic_write_text(METADATA_DIR / "checksums.sha256", "\n".join(checksum_lines) + "\n", overwrite=True)
    atomic_write_json(
        METADATA_DIR / "artifacts.json",
        {"validated_at": iso_now(), "status": "PASS", "artifacts": artifacts},
        overwrite=True,
    )
    print(f"Validação: PASS ({len(segments)} segmentos; {duration / 60:.1f} minutos)")
    return 0


def command_list_files(_: argparse.Namespace) -> int:
    candidates = set(final_artifact_paths())
    candidates.update(
        path for path in METADATA_DIR.glob("*")
        if path.is_file() and path.name != ".gitkeep"
    )
    rows = []
    for path in sorted(candidates):
        if path.is_file() and path.name != ".gitkeep":
            rows.append((str(path.relative_to(PROJECT_DIR)), human_size(path.stat().st_size)))
    if not rows:
        print("Nenhum artefato de execução criado.")
        return 0
    width = max(len(path) for path, _ in rows)
    for path, size in rows:
        print(f"{path:<{width}}  {size:>10}")
    return 0


def command_run(args: argparse.Namespace) -> int:
    if not args.allow_network:
        print("Execução completa bloqueada: use --allow-network após autorização.", file=sys.stderr)
        return 2
    status = command_download(argparse.Namespace(allow_network=True))
    if status:
        return status
    command_normalize(argparse.Namespace())
    try:
        command_convert_model(argparse.Namespace())
    except Exception as exc:
        print(f"AVISO: faster-whisper indisponível ({exc}); será usado transformers.", file=sys.stderr)
    status = command_transcribe(
        argparse.Namespace(
            backend="auto",
            allow_model_download=args.allow_model_download,
            device=args.device,
        )
    )
    if status:
        return status
    status = command_translate(
        argparse.Namespace(allow_model_download=args.allow_model_download, device=args.device)
    )
    if status:
        return status
    return command_validate(argparse.Namespace())


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    preflight = subparsers.add_parser("preflight", help="Inventaria ferramentas e modelos sem rede.")
    preflight.add_argument("--strict", action="store_true")
    preflight.set_defaults(func=command_preflight)

    download = subparsers.add_parser("download", help="Baixa somente o áudio; YouTube antes do X.")
    download.add_argument("--allow-network", action="store_true")
    download.set_defaults(func=command_download)

    normalize = subparsers.add_parser("normalize", help="Converte o áudio para WAV mono de 16 kHz.")
    normalize.set_defaults(func=command_normalize)

    convert_model = subparsers.add_parser("convert-model", help="Converte o Whisper em CTranslate2/INT8 sem rede.")
    convert_model.set_defaults(func=command_convert_model)

    transcribe = subparsers.add_parser("transcribe", help="Transcreve localmente em inglês.")
    transcribe.add_argument("--backend", choices=("auto", "faster-whisper", "transformers"), default="auto")
    transcribe.add_argument("--allow-model-download", action="store_true")
    transcribe.add_argument("--device", choices=("auto", "cpu", "mps"), default="auto")
    transcribe.set_defaults(func=command_transcribe)

    translate = subparsers.add_parser("translate", help="Traduz localmente do inglês para o português.")
    translate.add_argument("--allow-model-download", action="store_true")
    translate.add_argument("--device", choices=("auto", "cpu", "mps"), default="auto")
    translate.set_defaults(func=command_translate)

    render = subparsers.add_parser("render", help="Gera TXT, SRT e Markdown a partir dos segmentos.")
    render.add_argument("--replace-generated", action="store_true", help="Substitui somente arquivos derivados em outputs/.")
    render.set_defaults(func=command_render)

    validate = subparsers.add_parser("validate", help="Valida cobertura, timestamps, arquivos e hashes.")
    validate.set_defaults(func=command_validate)

    list_files = subparsers.add_parser("list-files", help="Lista artefatos e tamanhos.")
    list_files.set_defaults(func=command_list_files)

    run = subparsers.add_parser("run", help="Executa o pipeline completo após autorização.")
    run.add_argument("--allow-network", action="store_true")
    run.add_argument("--allow-model-download", action="store_true")
    run.add_argument("--device", choices=("auto", "cpu", "mps"), default="auto")
    run.set_defaults(func=command_run)
    return parser


def main(argv: Iterable[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(list(argv) if argv is not None else None)
    try:
        return int(args.func(args))
    except (FileExistsError, FileNotFoundError, RuntimeError, ValueError) as exc:
        print(f"ERRO: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
