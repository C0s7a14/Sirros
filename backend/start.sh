#!/bin/bash
set -e
python -m alembic upgrade a7d4c33dddeb
python -m alembic upgrade c3f1a2b4e5d6
exec uvicorn app.main:app --host 0.0.0.0 --port "${PORT:-8000}"
