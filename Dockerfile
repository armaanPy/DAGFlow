FROM apache/airflow:2.9.3

RUN curl -sSL https://install.python-poetry.org | python3 && \
    export PATH=$PATH:/root/.local/bin && \
    poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock* /opt/airflow/

WORKDIR /opt/airflow

RUN poetry install --no-root

USER airflow