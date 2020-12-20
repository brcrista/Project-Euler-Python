# Project Euler

[![GitHub Actions build badge](https://github.com/brcrista/Project-Euler-Python/workflows/CI/badge.svg)](https://github.com/brcrista/Project-Euler-Python/actions?query=workflow%3ACI)

<https://projecteuler.net>

## Prerequisities

- Python 3.6 or later

## Setup

```bash
# Optional: create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

source set_python_env.sh
```

## Checking solutions

Each solution can be run individually. For example, to see the solution to Problem 1, do

```bash
script/solution 1
```

Each solution has a test suite that checks the actual solution and possibly some other properties. To run all tests, do

```bash
script/test
```