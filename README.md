# Insurance RAG Assistant

## Guide for project setup at first

```text
Install python
Install pip
pip install uv
uv init --package
uv add --dev httpx ruff mypy pytest pre-commit
uv add fastapi "uvicorn[standard]" pydantic-settings
Add pre-commit-config.yaml file
uv run pre-commit autoupdate
uv run pre-commit install
uv run pre-commit run --all-files
```
```shell
```

## Setup

```shell
uv sync
uv run pre-commit install
```

## Test

```shell
uv run pytest
```
```shell
uv run uvicorn app_rag_assistant.main:app --reload
```

```shell
curl http://127.0.0.1:8000/health
```
```shell
curl http://127.0.0.1:8000/docs
```

## Quality Check

```shell
uv run ruff check .
uv run mypy
```
