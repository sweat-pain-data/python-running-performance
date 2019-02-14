.PHONY: lint test build upload-test upload

all: lint test

lint:
	flake8

test:
	python -m pytest --cov=running_performance --cov-report term-missing:skip-covered

build:
	./setup.py sdist bdist_wheel

upload-test: lint test build
	python -m twine upload --skip-existing --repository-url https://test.pypi.org/legacy/ dist/*

upload: lint test build
	python -m twine upload dist/*
