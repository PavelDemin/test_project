FROM python:3.9.7-slim

ENV PYTHONUNBUFFERED=1
COPY pyproject.toml poetry.lock /
RUN pip3 install poetry
ENV POETRY_VIRTUALENVS_CREATE false
RUN poetry install

COPY . /app

WORKDIR /app
CMD poetry run alembic upgrade head && cd src && poetry run uvicorn --host=0.0.0.0 --port=8080 main:app
