.PHONY: all
all: dependencies typecheck tests sdist wheel

.PHONY: clean
clean:
	git clean -xdf -e .venv

.PHONY: dependencies
dependencies:
	pip install -r requirements-dev.txt

.PHONY: typecheck
typecheck:
	mypy src --strict

.PHONY: tests
tests:
	pytest --doctest-modules