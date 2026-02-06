PYTHON ?= python3
VENV ?= .venv
PIP := $(VENV)/bin/pip
PY := $(VENV)/bin/python

.PHONY: setup check run

setup:
	$(PYTHON) -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

check:
	test -f jury.json || cp jury.example.json jury.json
	test -f jobs.json || cp jobs.example.json jobs.json
	$(PY) run_jury.py --config jury.json --task "make check"
	$(PY) scheduler.py --jobs jobs.json

run:
	test -f jury.json || cp jury.example.json jury.json
	$(PY) run_jury.py --config jury.json --task "hello"
