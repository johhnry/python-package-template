# Python package template

This repository is a Python package template that uses modern tooling and packaging like [Poetry](https://python-poetry.org/), [Mypy](https://mypy.readthedocs.io/en/stable/), [Ruff](https://github.com/charliermarsh/ruff)...

This is intended to be a demonstration of how good Python tooling and DX became over the years.

# Tools

- [Poetry](https://python-poetry.org/): dependency and virtualenv management
- [Mypy](https://mypy.readthedocs.io/en/stable/): PEP484 compliant static type checker
- [Ruff](https://github.com/charliermarsh/ruff): an extremely fast Python linter, written in Rust
- [Black](https://black.readthedocs.io/en/stable/): the uncompromising Python code formatter
- [Isort](https://pycqa.github.io/isort/index.html): sort Python imports automatically
- [Pytest](https://docs.pytest.org/en/7.2.x/) (+ [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/readme.html) code coverage): unit test runner
- [Pre-commit](https://pre-commit.com/): multi-language pre-commit Git hooks

# Usage

First install the dependencies:

```shell
$ poetry config virtualenvs.in-project true # Use .venv folder in project
$ poetry install
```

Then with the help of [Poe the Poet](https://github.com/nat-n/poethepoet), a task runner for Poetry similar to NodeJS's `package.json` scripts, you can launch different actions:

```
$ poetry run poe --help

CONFIGURED TASKS
  test           Run tests with code coverage
  format-check   Check code style
  lint-check     Lint code
  type-check     Static type checking
  imports-check  Check import order
  check-all
```
