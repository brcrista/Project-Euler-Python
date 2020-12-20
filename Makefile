.PHONY: all
all: dependencies typecheck tests sdist wheel

.PHONY: clean
clean:
	rm -rf **/.mypy_cache/
	rm -rf **/.pytest_cache/
	rm -rf **/__pycache__/
	rm -rf junit/

.PHONY: dependencies
dependencies:
	pip install -r requirements-dev.txt

.PHONY: typecheck
typecheck:
	mypy src --strict

.PHONY: tests
tests:
	pytest --doctest-modules --junitxml=junit/test-results.xml