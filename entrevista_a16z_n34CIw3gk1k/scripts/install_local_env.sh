#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

if [[ "${1:-}" != "--allow-network" ]]; then
  echo "Instalação bloqueada: execute novamente com --allow-network somente após autorização e em conexão adequada." >&2
  exit 2
fi

if ! command -v ffmpeg >/dev/null 2>&1 || ! command -v ffprobe >/dev/null 2>&1; then
  if ! command -v brew >/dev/null 2>&1; then
    echo "ffmpeg/ffprobe ausentes e Homebrew não encontrado." >&2
    exit 1
  fi
  brew install ffmpeg
fi

PYTHON_BIN="$(command -v python3)"
if ! command -v uv >/dev/null 2>&1; then
  echo "uv não encontrado. Instale-o ou crie o ambiente manualmente conforme o README." >&2
  exit 1
fi

cd "$PROJECT_DIR"
if [[ ! -x .venv/bin/python ]]; then
  uv venv --python "$PYTHON_BIN" .venv
fi

uv pip install --python .venv/bin/python -r requirements.in
uv pip freeze --python .venv/bin/python > requirements.lock.txt

echo "Ambiente local preparado em $PROJECT_DIR/.venv"
echo "Versões fixadas em $PROJECT_DIR/requirements.lock.txt"
