---
description: Use Rich for CLI scripts under scripts/
globs: scripts/**/*.py
alwaysApply: false
---

# CLI scripts — use Rich + rich-click

Scripts under `scripts/` are CLI tools (spikes, one-off checks). Use:

- [Rich](https://rich.readthedocs.io/) for terminal output — not bare `print()`
- [rich-click](https://github.com/ewels/rich-click) for CLI parsing — not `argparse` (`import rich_click as click`)

Rich helpers:

- `rich.console.Console` for styled messages, errors, and success lines
- `rich.panel.Panel` for multi-line prompts (e.g. device-code sign-in)
- `rich.syntax.Syntax` for JSON or structured payloads
- Color HTTP status codes: green `< 400`, red `>= 400`

Interactive UIs belong in `streamlit/pages/` and call into `src/clarify/` adapters plus spike scripts — not dual-mode
entry points in the same file.

Add `rich` and `rich-click` under `[project.optional-dependencies] dev` if not already present.
