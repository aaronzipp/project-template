SHELL := /bin/bash

init:
	sudo apt update
	sudo apt upgrade -y
	sudo apt install libjpeg-dev \
		zlib1g-dev \
		libpng-dev \
		libxml2-dev \
		libxslt-dev
	python3 -m venv .
	source ./bin/activate && \
		python3 -m pip install -r requirements.txt && \
		pre-commit install && \
		curl https://raw.githubusercontent.com/codelucas/newspaper/master/download_corpora.py | python3
