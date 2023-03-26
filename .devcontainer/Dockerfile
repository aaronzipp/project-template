ARG VARIANT=3.10
FROM mcr.microsoft.com/vscode/devcontainers/python:${VARIANT}

RUN python -m pip install --upgrade pip && \
	pip install --no-cache-dir poetry

COPY poetry.lock pyproject.toml ./
RUN poetry install
