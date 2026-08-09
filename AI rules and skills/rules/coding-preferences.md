---
description: 
globs: 
alwaysApply: true
---

# Coding Pattern Preferences

- Always prefer simple solutions.
- Avoid duplicating code — check whether similar functionality already exists elsewhere in the codebase before writing something new.
- Write code that accounts for the different environments: dev, test, and prod.
- When fixing a bug, exhaust the options within the existing implementation before introducing a new pattern or technology. If you do introduce one, remove the old implementation afterward so there's no duplicate logic.
- Keep the codebase clean and organized.
- Avoid writing one-off scripts into files where possible, especially scripts likely to run only once.
- Keep files under ~200–300 lines of code; refactor once you cross that.
- Mock data is only needed for tests — never mock data for dev or prod.
- Never add stubbing or fake-data patterns to code that affects dev or prod.
- Never overwrite the `.env` file without asking and getting confirmation first.
- Where appropriate, prefer subclassing and method overrides over if/else branching for special cases.

# Workflow Preferences

- Stay scoped to the requested change: only make changes that are requested, or that you're confident are well-understood and related. Don't touch unrelated code, and don't fix typos, refactor, or add comments outside the task unless it's necessary to complete it.
- Avoid major changes to a feature's working patterns or architecture once it's proven to work, unless explicitly instructed.
- Always think about what other methods and areas of code might be affected by a change.

# Testing

- Write thorough, clear tests covering all major functionality, organized so specific tests are easy to find and run.
- Test your own code and logic — not the language or framework itself.

# Python Style

- Use f-strings (or t-strings for templated/deferred cases) rather than `str.format()` or `%` formatting.
- Prefer built-in generic types over `typing` equivalents (`list` over `List`, `dict` over `Dict`).
- Prefer `X | None` over `typing.Optional[X]`.
- Remove unused imports.
- Prefer single quotes where PEP 8 allows.
- Prefer single-line statements over multi-line where it doesn't hurt readability (PEP 8 permitting).
