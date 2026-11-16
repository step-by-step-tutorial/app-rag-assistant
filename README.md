# Insurance RAG Assistant

## Installation

```shell
pip install uv
```

## Setup

```shell
uv init --package
```

```shell
uv add --dev ruff mypy pytest pre-commit
```

```shell
uv run pre-commit autoupdate
```

```shell
uv run pre-commit install
```

```shell
uv run pre-commit run --all-files
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
