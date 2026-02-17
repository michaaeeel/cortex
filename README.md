# Cortex

AI-Powered Campaign Intelligence Platform. Ingest advertising data from multiple sources, process it through ML pipelines, and get actionable insights through a web dashboard and automated reports.

## Architecture

| Service | Tech | Port |
|---------|------|------|
| Backend API | Django + DRF | 8000 |
| Frontend | React + Vite | 5173 |
| ML Services | FastAPI | 8001 |
| Data Pipeline | Celery | -- |
| Database | PostgreSQL | 5432 |
| Cache/Broker | Redis | 6379 |
| Reverse Proxy | Nginx | 80 |

## Quick Start

```bash
# Configure environment
cp .env.example .env

# Start all services
docker compose up --build

# Run database migrations
docker compose exec backend python manage.py migrate

# Create admin user
docker compose exec backend python manage.py createsuperuser
```

Then visit:
- **App**: http://localhost:5173
- **API**: http://localhost:8000/api/v1/
- **Admin**: http://localhost:8000/admin/
- **ML Docs**: http://localhost:8001/docs

## Project Structure

```
cortex/
├── backend/          # Django REST API
├── frontend/         # React SPA
├── ml-services/      # FastAPI ML microservice
├── data-pipeline/    # Celery workers for data ingestion
├── infrastructure/   # Nginx config
├── docs/             # Architecture docs
└── docker-compose.yml
```

See [docs/architecture.md](docs/architecture.md) for detailed documentation.
