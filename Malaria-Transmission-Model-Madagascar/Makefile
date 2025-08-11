# Makefile for Malaria Transmission Model
# Common development tasks

.PHONY: help install test lint format clean run example docs

help:
	@echo "Malaria Transmission Model - Available Commands"
	@echo "================================================"
	@echo "install     - Install dependencies"
	@echo "test        - Run tests"
	@echo "lint        - Run code quality checks"
	@echo "format      - Format code with Black"
	@echo "clean       - Remove generated files"
	@echo "run         - Run main simulation"
	@echo "example     - Run quick example"
	@echo "docs        - Generate documentation"
	@echo "all         - Install, test, and lint"

install:
	pip install -r requirements.txt
	pip install -e .

install-dev:
	pip install -r requirements.txt
	pip install -e ".[dev]"

test:
	pytest tests/ -v --cov=src --cov-report=html --cov-report=term

lint:
	flake8 src/ tests/ --max-line-length=100 --ignore=E203,W503
	
format:
	black src/ tests/ main.py example_usage.py

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache/
	rm -rf htmlcov/
	rm -rf .coverage
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete

run:
	python main.py

example:
	python example_usage.py

docs:
	@echo "Documentation available in docs/ directory"
	@echo "Main documentation: docs/model_description.md"

all: install-dev lint test
	@echo "All checks passed!"

