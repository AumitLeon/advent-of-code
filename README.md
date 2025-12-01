# Advent of Code

Solutions for Advent of Code challenges across multiple years.

## Structure
- `2024/` - Solutions for Advent of Code 2024
  - Each day's solution is in its own directory: `day_01/`, `day_02/`, etc.
  - Each directory contains:
    - `solution.py` - The solution code
    - `test_solution.py` - Tests for the solution
    - `input.txt` - Puzzle input 

## Installation

This repo uses Nix and `uv` for Python package management.

### Prerequisites
- [Nix](https://nixos.org/download.html) with flakes enabled
- Optional: [direnv](https://direnv.net/) for automatic environment activation

### Setup

1. Enter the development environment:
   ```bash
   nix develop
   ```

2. Sync dependencies with uv:
   ```bash
   uv sync
   ```

The Nix flake automatically activates the virtual environment (`.venv`) if it exists.

### Using direnv (Optional)

This repo uses [direnv](https://direnv.net/) to automatically activate the Nix shell when you `cd` into the repo (see `.envrc`). Whitelist the repo to enable automatic activation:

```bash
direnv allow
```

## Running Solutions

From within a specific day directory:
```bash
cd 2024/day_01
python solution.py
```

## Running Tests

Run all tests:
```bash
uv run pytest
```

Run tests for a specific day:
```bash
cd 2024/day_01
pytest
```

Run tests with verbose output:
```bash
uv run pytest -v
``` 
