.PHONY: test

all: lint test

lint:
	flake8

test:
	python -m pytest --cov=running_performance --cov-report term-missing:skip-covered
