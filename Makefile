.PHONY: install test test-ex1 test-ex2 test-ex3 coverage coverage-all clean

PYTHON ?= python3
VENV := .venv
PYTEST := $(VENV)/bin/pytest

install:
	$(PYTHON) -m venv $(VENV)
	$(VENV)/bin/pip install --upgrade pip
	$(VENV)/bin/pip install -r requirements.txt

test:
	$(PYTEST)

test-ex1:
	$(PYTEST) exercicio1_triangulo

test-ex2:
	$(PYTEST) exercicio2_person

test-ex3:
	$(PYTEST) exercicio3_salario

coverage:
	$(PYTEST) exercicio1_triangulo --cov=exercicio1_triangulo --cov-report=term-missing --cov-report=html:htmlcov/exercicio1_triangulo
	$(PYTEST) exercicio2_person --cov=exercicio2_person --cov-report=term-missing --cov-report=html:htmlcov/exercicio2_person
	$(PYTEST) exercicio3_salario --cov=exercicio3_salario --cov-report=term-missing --cov-report=html:htmlcov/exercicio3_salario

coverage-all:
	$(PYTEST) --cov=. --cov-report=term-missing --cov-report=html:htmlcov/total

clean:
	rm -rf .pytest_cache htmlcov .coverage
	find . -name '__pycache__' -type d -prune -exec rm -rf {} +
