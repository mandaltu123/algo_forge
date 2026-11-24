# AlgoForge — Python

> Don't memorize solutions. Master the patterns.

A comprehensive repository of data structures, algorithms, problem-solving patterns and optimized Python implementations.

## Prerequisites

- macOS
- Python 3.11 or newer
- PyCharm
- Git

## Virtual environment setup

### 1. Navigate to the project

```bash
cd /Users/tsm/work/november2026/algo_forge
```

### 2. Verify Python installation

```bash
python3 --version
which python3
```

### 3. Create the virtual environment (first time only)

```bash
python3 -m venv .venv
```

### 4. Activate / enable the virtual environment

```bash
source .venv/bin/activate
```

The terminal prompt should display `(.venv)`.

### 5. Verify the active environment

```bash
which python
python --version
python -m pip --version
```

The Python executable should point to `.venv/bin/python` inside the project.

### 6. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install pytest
```

### 7. Save dependencies

```bash
python -m pip freeze > requirements.txt
```

### 8. Deactivate / disable the virtual environment

```bash
deactivate
```

### 9. Reactivate the virtual environment

Whenever you open a new terminal:

```bash
cd /Users/tsm/work/november2026/algo_forge
source .venv/bin/activate
```

Do not recreate the environment every time.

### 10. Recreate the virtual environment (optional)

If the environment is corrupted or needs to be reset, deactivate it first if active. From the project root, run:

```bash
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Ensure `requirements.txt` exists before resetting the environment.

## Configure PyCharm

1. Open PyCharm > Settings (`Cmd + ,`).
2. Search for Python Interpreter.
3. Select Add Interpreter > Add Local Interpreter.
4. Choose an existing virtual environment and select:
   `/Users/tsm/work/november2026/algo_forge/.venv/bin/python`
5. Apply the settings.

PyCharm can automatically activate the environment in new integrated terminals. Check Settings > Tools > Terminal > Activate virtualenv if necessary.

## Run Python programs

```bash
python arrays/two_sum.py
```

## Run unit tests

```bash
python -m pytest -v
```

## Git workflow

```bash
git status
git add .
git commit -m "Implement algorithm with tests"
git push origin main
```

## Problem-solving approach

For each problem, document:

- Problem statement and source link
- Brute-force solution
- Optimized solution and algorithmic pattern
- Time and space complexity
- Edge cases and unit tests

**Discipline. Precision. Mastery.**
