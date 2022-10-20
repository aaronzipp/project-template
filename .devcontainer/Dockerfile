ARG VARIANT=3.9
FROM mcr.microsoft.com/vscode/devcontainers/python:${VARIANT}

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
    libjpeg-dev \
		zlib1g-dev \
		libpng-dev \
		libxml2-dev \
		libxslt-dev 

COPY requirements.txt /tmp/pip-tmp/
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
&& rm -rf /tmp/pip-tmp
RUN curl https://raw.githubusercontent.com/codelucas/newspaper/master/download_corpora.py | python3
COPY .pre-commit-config.yaml .
