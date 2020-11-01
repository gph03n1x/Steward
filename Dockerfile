FROM python:3.8.5

RUN adduser --uid 1000 --disabled-password --gecos '' --home /home/deploy deploy

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gettext \
    libpq-dev \
    netcat \
    postgresql-client && \
    pip install --upgrade pip && \
    rm -rf /var/lib/apt/lists/*

RUN pip install poetry
RUN poetry config virtualenvs.create false

WORKDIR /app

COPY pyproject.toml /app
RUN poetry install --no-dev

COPY . /app

RUN chown -R deploy:deploy /app
USER deploy

CMD ["python", "-m", "steward.main"]