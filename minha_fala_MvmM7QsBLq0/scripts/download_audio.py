#!/usr/bin/env python3
"""Baixa somente o áudio arquivado do vídeo solicitado.

Fonte: https://www.youtube.com/live/MvmM7QsBLq0
Método: página pública /live + manifesto do player; sem cookies, playlist ou API key.
"""

from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
META = ROOT / "metadata"
PAGE = META / "live_page.html"
VIDEO_ID = "MvmM7QsBLq0"
SOURCE = f"https://www.youtube.com/live/{VIDEO_ID}"


def get_player_response() -> dict:
    request = Request(SOURCE, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(request, timeout=60) as response:
        html = response.read().decode("utf-8", errors="replace")
    PAGE.write_text(html, encoding="utf-8")
    match = re.search(r"ytInitialPlayerResponse\s*=\s*(\{.*?\});", html, re.S)
    if not match:
        raise RuntimeError("ytInitialPlayerResponse não encontrado na página /live")
    return json.loads(match.group(1))


def main() -> int:
    RAW.mkdir(parents=True, exist_ok=True)
    META.mkdir(parents=True, exist_ok=True)
    player = get_player_response()
    formats = player["streamingData"]["adaptiveFormats"]
    audio = next(item for item in formats if item.get("itag") == 140)
    url = audio["url"]
    metadata = {
        "source_url": SOURCE,
        "video_id": VIDEO_ID,
        "retrieved_at_utc": datetime.now(timezone.utc).isoformat(),
        "title": player.get("videoDetails", {}).get("title"),
        "duration_seconds": player.get("videoDetails", {}).get("lengthSeconds"),
        "playability_status": player.get("playabilityStatus"),
        "audio_format": {k: audio.get(k) for k in ("itag", "mimeType", "bitrate", "targetDurationSec", "maxDvrDurationSec")},
        "download_method": "public /live player manifest, audio-only itag 140",
        "credentials": False,
    }
    (META / "source_run.json").write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    output = RAW / f"{VIDEO_ID}.m4a"
    print("Baixando somente áudio (itag 140)...", flush=True)
    request = Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0",
            "Accept": "*/*",
            "Referer": SOURCE,
            "Origin": "https://www.youtube.com",
        },
    )
    try:
        with urlopen(request, timeout=60) as response, output.open("wb") as handle:
            total = 0
            while True:
                chunk = response.read(1024 * 1024)
                if not chunk:
                    break
                handle.write(chunk)
                total += len(chunk)
                if total % (10 * 1024 * 1024) < len(chunk):
                    print(f"  {total / 1024 / 1024:.1f} MiB", flush=True)
    except Exception as exc:
        print(f"Download falhou: {exc}", file=sys.stderr)
        return 1
    if not output.exists() or output.stat().st_size == 0:
        raise RuntimeError("download produziu arquivo vazio")
    print(f"Áudio bruto salvo em {output} ({output.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
