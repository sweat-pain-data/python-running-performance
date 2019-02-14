.PHONY: test build

all: lint test

lint:
	flake8

test:
	python -m pytest --cov=running_performance --cov-report term-missing:skip-covered

build: test
	./setup.py sdist bdist_wheel

upload-test: build
	python3 -m twine upload --skip-existing --repository-url https://test.pypi.org/legacy/ dist/*
