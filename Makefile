SHELL=bash

env:
	virtualenv venv

install:
	pip install -r requirements.txt

activate:
	source venv/bin/activate

run:
	python main.py