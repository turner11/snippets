---
description: Enforce the use of Astral's uv tool for Python project creation, dependency management, and script execution. Prevents standard pip/venv/poetry workflows.
globs: "*.py", "pyproject.toml", "uv.lock"
---

# Python Virtual Environment and Dependency Rule

## Core Directive
ALWAYS use `uv` for all Python environments, package management, and script executions. NEVER use legacy tools like `pip`, `venv`, `poetry`, `pipenv`, or standard `python` activation scripts.

## Environment Management Rules
- **NEVER** use `source .venv/bin/activate` or instruct the user to do so.
- **NEVER** use `python -m venv` or `virtualenv`.
- To initialize a project, always use: `uv init`
- To sync an existing environment, always use: `uv sync`

## Dependency Rules
- **NEVER** use `pip install` or `pip install -r requirements.txt`.
- To add packages, always use: `uv add <package_name>`
- To add dev dependencies, always use: `uv add --dev <package_name>`
- To remove packages, always use: `uv remove <package_name>`

## Execution Rules
- **NEVER** run bare python scripts (e.g., `python main.py`).
- Always wrap execution commands in `uv run`.
- Example: `uv run main.py`
- Example for notebooks: `uv run jupyter lab`

## Output formatting
When writing terminal commands for the user in chat responses, strictly adhere to the `uv run` format. Highlight the elimination of manual activation steps if the user asks why.