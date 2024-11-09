FROM python:3.9-slim

WORKDIR /DAGFlow

RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    libpq-dev \
    gcc \
    git \
    && apt-get clean

RUN pip install poetry==1.8.3

COPY pyproject.toml poetry.lock /DAGFlow/
COPY . /DAGFlow/

RUN poetry install --no-root && ln -s $(poetry env info --path) ~/venv