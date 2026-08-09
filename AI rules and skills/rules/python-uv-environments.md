---
description: Use Astral uv for Python virtualenvs and installs in this repo
alwaysApply: true
---

# Python environments (uv)

- **Create environments** with `uv venv` (or `uv venv .venv`). Do not use `python -m venv` for new envs.
- **Install dependencies** with `uv pip install -r requirements.txt`, `uv pip sync` (when a lockfile exists), or `uv sync` in a `pyproject.toml` project. Prefer `uv` over plain `pip install` for project work.
- **Run tools** via `uv run <command>` when helpful so commands use the project interpreter without manual activation.
- **Docker / CI**: install the `uv` binary (e.g. copy from `ghcr.io/astral-sh/uv`) and prefer `uv pip install --system` (or `uv sync --system`) into the container’s system Python instead of creating a venv inside the image, unless a venv is explicitly required.
