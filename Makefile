PYTHON = python3
PIP = ${PYTHON} -m pip
PY_TEST = ${PYTHON} -m pytest

MARK ?= ""
COVERAGE_OPTS ?=
PYTHONPATH = "./src"

.PHONY: default
default: test

.PHONY: deps
deps:
	${PIP} install -r requirements.txt

.PHONY: test
test:
	${PY_TEST} -m ${MARK}

.PHONY: coverage
coverage:
	${PY_TEST} -m ${MARK} --cov-config .coveragerc --cov=./ --cov-report html:htmlcov ${COVERAGE_OPTS}
