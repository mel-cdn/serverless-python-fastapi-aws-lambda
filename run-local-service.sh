#!/usr/bin/env bash

set -e -u

export PYTHONPATH=src

echo "> Running local FastAPI service on http://0.0.0.0:8000 "
uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
echo "> Done!"
