# Entrevista a16z — download e transcrição local

Pipeline preparado para a entrevista indicada por `n34CIw3gk1k`. A fonte preferencial é o YouTube; o post do X é consultado apenas se o YouTube falhar. O áudio nunca é enviado a um serviço externo e nenhuma API key é usada.

## Estado em 11 de agosto de 2026

Trabalho concluído e validado localmente. O YouTube foi tentado primeiro, mas
respondeu com HTTP 429 e exigência de confirmação contra robôs. Sem recorrer a
cookies ou contornar a proteção, o pipeline usou o fallback oficial do X. O
arquivo obtido contém somente áudio AAC, sem fluxo de vídeo, e dura 36min31s.

Inventário final verificado:

| Item | Estado |
|---|---|
| Mac | Apple M3 Max, 36 GB de memória, macOS 14.7.3 |
| Espaço disponível | aproximadamente 271 GB na unidade de dados |
| `yt-dlp` | `2026.7.4`, instalado apenas no `.venv` do projeto |
| `ffmpeg` / `ffprobe` | já estavam instalados; `ffmpeg 8.0` |
| Python / `uv` | Python `3.13.3`; `uv 0.9.28` |
| Whisper | `faster-whisper 1.2.1`; `ctranslate2 4.8.1` |
| Tradução | `transformers 4.56.1`; `torch 2.11.0`; `mlx-lm 0.29.1`; `mlx 0.32.0` |
| Modelo Whisper | `openai/whisper-large-v3-turbo`, convertido para CTranslate2/INT8 |
| Modelos de tradução | NLLB-200 600M, Unicamp EN–PT T5 e Qwen3-8B 4-bit, todos executados localmente |

## Modelo escolhido

Foi usado o **Whisper large-v3-turbo** com `faster-whisper`, convertido para
CTranslate2/INT8 e executado localmente na CPU. A escolha preserva boa qualidade
do modelo large, exige menos memória e é mais rápida que o `large-v3` completo.
O arquivo bruto do primeiro passe foi preservado. Uma verificação independente
do encerramento eliminou três microsegmentos fisicamente impossíveis; a decisão
está documentada em `metadata/TRANSCRIPTION_REVIEW.md`.

A tradução final combina duas traduções locais — NLLB-200 distilled 600M e o
modelo EN–PT T5 da Unicamp — com duas revisões pelo Qwen3-8B 4-bit em MLX. A
primeira comparou o inglês com os dois rascunhos; a segunda usou somente o
contexto dos dois segmentos vizinhos de cada lado. Uma revisão editorial final
corrigiu 124 calques, termos técnicos e vazamentos entre segmentos, todos
registrados em `metadata/translation_corrections.tsv`. Os rascunhos e passes
intermediários foram preservados para auditoria.

## Como repetir no futuro

Em conexão adequada e depois de autorizar acesso à rede:

```bash
cd "/Users/manoelgaldino/Documents/DCP/Papers/IA agents methodology/entrevista_a16z_n34CIw3gk1k"
bash scripts/install_local_env.sh --allow-network
.venv/bin/python scripts/pipeline.py preflight --strict
.venv/bin/python scripts/pipeline.py run --allow-network --allow-model-download
```

O comando `run` executa, nesta ordem: YouTube, fallback para X somente se necessário, normalização por `ffmpeg`, conversão local do Whisper, transcrição, tradução, renderização e validação. Os indicadores `--allow-network` e `--allow-model-download` são guardas deliberadas contra uso acidental da rede.

Para repetir por etapas:

```bash
.venv/bin/python scripts/pipeline.py download --allow-network
.venv/bin/python scripts/pipeline.py normalize
.venv/bin/python scripts/pipeline.py convert-model
.venv/bin/python scripts/pipeline.py transcribe --backend auto
.venv/bin/python scripts/pipeline.py translate --allow-model-download
.venv/bin/python scripts/pipeline.py translate-br --allow-model-download
.venv/bin/python scripts/pipeline.py translate-br-context --allow-model-download
.venv/bin/python scripts/pipeline.py finalize-translation
.venv/bin/python scripts/pipeline.py render
.venv/bin/python scripts/pipeline.py validate
.venv/bin/python scripts/pipeline.py list-files
```

## Identificação de falantes

O Whisper não identifica pessoas. `metadata/speakers.tsv` registra `Alejandro`
somente em respostas sustentadas pela estrutura da entrevista e `Host` nas
perguntas/apresentações. A fonte oficial confirma Angela Strange, Gabriel
Vasquez e Alejandro Maza, mas não oferece diarização; por isso Angela e Gabriel
não foram distinguidos entre si. Cada intervalo nominal inclui evidência.

Depois de revisar `metadata/speakers.tsv`, regenere apenas os arquivos derivados:

```bash
.venv/bin/python scripts/pipeline.py render --replace-generated
.venv/bin/python scripts/pipeline.py validate
```

## Arquivos finais

| Arquivo | Conteúdo |
|---|---|
| `outputs/transcricao_ingles.txt` | transcrição integral em inglês |
| `outputs/transcricao_ingles.srt` | transcrição em inglês com timestamps |
| `outputs/transcricao_ingles.md` | transcrição em inglês em blocos de cinco minutos |
| `outputs/traducao_portugues.md` | tradução integral em português nos mesmos blocos |
| `metadata/segmentos_whisper_raw.json` | primeiro passe bruto e imutável do Whisper |
| `metadata/segmentos_whisper.json` | 425 segmentos revisados, tempos e metadados do modelo |
| `metadata/segmentos_traducao_nllb.json` | primeira tradução local, pelo NLLB |
| `metadata/segmentos_traducao_unicamp.json` | segunda tradução local, pelo modelo da Unicamp |
| `metadata/segmentos_traducao_br.json` | primeira revisão local em português brasileiro |
| `metadata/segmentos_traducao_br_contexto.json` | segunda revisão, com contexto dos segmentos vizinhos |
| `metadata/segmentos_traducao_final.json` | tradução final, alinhada 1:1 e pós-editada |
| `metadata/translation_corrections.tsv` | 124 correções editoriais reproduzíveis com justificativa |
| `metadata/checksums.sha256` | hashes dos artefatos preservados |
| `metadata/artifacts.json` | lista final, tamanhos e hashes |

O áudio baixado permanece imutável em `data/raw/`. A cópia WAV mono de 16 kHz usada pelos modelos fica em `data/processed/`. O pipeline se recusa a sobrescrever artefatos existentes por padrão.

## Comandos executados

Os comandos principais foram:

```bash
bash scripts/install_local_env.sh --allow-network
.venv/bin/python scripts/pipeline.py preflight --strict
.venv/bin/python scripts/pipeline.py download --allow-network
.venv/bin/python scripts/pipeline.py normalize
.venv/bin/python scripts/pipeline.py convert-model
.venv/bin/python scripts/pipeline.py transcribe --backend faster-whisper
.venv/bin/python scripts/pipeline.py translate --allow-model-download
.venv/bin/python scripts/pipeline.py translate-br --allow-model-download
.venv/bin/python scripts/pipeline.py translate-br-context --allow-model-download
.venv/bin/python scripts/pipeline.py finalize-translation
.venv/bin/python scripts/pipeline.py render --replace-generated
.venv/bin/python scripts/pipeline.py validate
.venv/bin/python -m unittest discover -s tests -v
uv pip check --python .venv/bin/python
```

As invocações externas de `yt-dlp`, `ffmpeg`, `ffprobe` e do conversor
CTranslate2 foram registradas literalmente em
`metadata/executed_commands.log`; saídas e erros ficaram em `logs/`. O áudio
nunca foi enviado a serviços externos e nenhuma API key foi usada.
