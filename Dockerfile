FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . app
COPY alembic app/alembic

EXPOSE 8000