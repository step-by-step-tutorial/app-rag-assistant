# Insurance RAG Assistant

## Guide for project setup at first

```text
Install python
Install pip
pip install uv
uv init --package
uv add --dev ruff mypy pytest pre-commit
Add pre-commit-config.yaml file
uv run pre-commit autoupdate
uv run pre-commit install
uv run pre-commit run --all-files
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

## Quality Check

```shell
uv run ruff check .
uv run mypy
```
