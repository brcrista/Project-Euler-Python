# Project Euler

[![GitHub Actions build badge](https://github.com/brcrista/Project-Euler-Python/workflows/CI/badge.svg)](https://github.com/brcrista/Project-Euler-Python/actions?query=workflow%3ACI)

<https://projecteuler.net>

## Prerequisities

- Python 3.6 or later

## Setup

```bash
source dev-env.sh
pip install -r requirements.txt
```

## Checking solutions

First, activate the dev environment with

```bash
source dev-env.sh
```

Each solution can be run individually. For example, to see the solution to Problem 1, do

```bash
script/solution 1
```

Each solution has a test suite that checks the actual solution and possibly some other properties. To run all tests, do

```bash
pytest
```