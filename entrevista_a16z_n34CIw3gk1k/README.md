# Entrevista a16z — download e transcrição local

Pipeline preparado para a entrevista indicada por `n34CIw3gk1k`. A fonte preferencial é o YouTube; o post do X é consultado apenas se o YouTube falhar. O áudio nunca é enviado a um serviço externo e nenhuma API key é usada.

## Estado em 11 de agosto de 2026

Nenhum URL foi acessado, nenhum pacote foi instalado e nenhum áudio ou modelo foi baixado nesta preparação.

Inventário local verificado:

| Item | Estado |
|---|---|
| Mac | Apple M3 Max, 36 GB de memória, macOS 14.7.3 |
| Espaço disponível | aproximadamente 271 GB na unidade de dados |
| `yt-dlp` | instalado; versão `2025.03.31`, que pode precisar de atualização antes do download |
| `ffmpeg` / `ffprobe` | instalados; `ffmpeg 8.0_1` |
| Python principal | `3.13.3` |
| `uv` | instalado |
| `torch` / `transformers` | instalados; versões `2.11.0` e `4.56.1` |
| `faster-whisper` / `ctranslate2` | ainda ausentes |
| Modelo Whisper | `openai/whisper-large-v3-turbo` completo no cache local, cerca de 1,5 GB |
| Modelo de tradução | `facebook/nllb-200-distilled-600M` ainda ausente |
| Python 3.11 do Homebrew | instalação local quebrada; o pipeline não depende dela |

## Modelo escolhido

O modelo principal será o **Whisper large-v3-turbo**, convertido localmente para CTranslate2/INT8 e executado pelo `faster-whisper` na CPU. Ele oferece melhor qualidade que as variantes `small` ou `medium`, mas é muito mais leve e rápido que o `large-v3` completo. Neste Mac, 36 GB de memória tornam o modelo confortável; a quantização INT8 reduz memória e tempo de execução. O modelo-base já está no cache, portanto a conversão não exige rede.

Se `faster-whisper` ou a conversão falhar, o script usa o mesmo modelo já armazenado via `transformers`. Para a tradução será usado localmente o NLLB-200 distilled 600M, com inglês (`eng_Latn`) como origem e português (`por_Latn`) como destino. O NLLB é um modelo específico de tradução e reduz o risco de resumir ou completar o texto como poderia ocorrer com um chatbot generativo.

## Execução futura

Somente depois de nova autorização e em conexão adequada:

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
.venv/bin/python scripts/pipeline.py render
.venv/bin/python scripts/pipeline.py validate
.venv/bin/python scripts/pipeline.py list-files
```

## Identificação de falantes

O Whisper não identifica pessoas. Depois da primeira transcrição, `metadata/speakers.tsv` deve ser preenchido somente com atribuições sustentadas pelo contexto ou pela audição local. Os nomes `Host`, `Angela`, `Gabriel` e `Alejandro` só podem ser usados com `confidence=high` e evidência explícita. Nos demais trechos, usam-se rótulos neutros como `Speaker 1`, `Speaker 2` etc. A etapa final inclui revisão desse arquivo antes de renderizar novamente os Markdown; o pipeline nunca inventa nomes.

Depois de revisar `metadata/speakers.tsv`, regenere apenas os arquivos derivados:

```bash
.venv/bin/python scripts/pipeline.py render --replace-generated
.venv/bin/python scripts/pipeline.py validate
```

## Arquivos finais previstos

| Arquivo | Conteúdo |
|---|---|
| `outputs/transcricao_ingles.txt` | transcrição integral em inglês |
| `outputs/transcricao_ingles.srt` | transcrição em inglês com timestamps |
| `outputs/transcricao_ingles.md` | transcrição em inglês em blocos de cinco minutos |
| `outputs/traducao_portugues.md` | tradução integral em português nos mesmos blocos |
| `metadata/segmentos_whisper.json` | segmentos originais, tempos e metadados do modelo |
| `metadata/segmentos_traducao.json` | correspondência entre blocos em inglês e português |
| `metadata/checksums.sha256` | hashes dos artefatos preservados |
| `metadata/artifacts.json` | lista final, tamanhos e hashes |

O áudio baixado permanece imutável em `data/raw/`. A cópia WAV mono de 16 kHz usada pelos modelos fica em `data/processed/`. O pipeline se recusa a sobrescrever artefatos existentes por padrão.

## Comandos já executados nesta preparação

Foram usados apenas comandos locais e sem rede: inventário de arquivos com `rg --files`; inspeção de hardware e espaço; `command -v`; consultas de versão de Python, `yt-dlp`, `ffmpeg` e pacotes; inspeção dos caches locais de modelos; `python3 -m unittest discover -s tests -v`; e o preflight `python3 scripts/pipeline.py preflight`. As guardas também foram testadas chamando `download` e `run` sem autorização de rede; ambas recusaram a execução. Os comandos de coleta efetivos serão registrados em `metadata/executed_commands.log`.
