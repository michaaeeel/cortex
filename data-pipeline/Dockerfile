FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN adduser --disabled-password --gecos "" --no-create-home appuser
USER appuser

CMD ["celery", "-A", "worker.app", "worker", "--loglevel=info"]
