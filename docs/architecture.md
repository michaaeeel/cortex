# Cortex Architecture

## Overview

Cortex is an AI-powered Campaign Intelligence Platform that ingests advertising data from multiple sources, processes it through ML pipelines, and delivers actionable insights through a web dashboard and automated reports.

## Architecture

```
                        ┌─────────────┐
                        │   Browser   │
                        └──────┬──────┘
                               │
                        ┌──────┴──────┐
                        │  Nginx :80  │
                        └──────┬──────┘
                               │
                ┌──────────────┼──────────────┐
                │              │              │
         ┌──────┴──────┐ ┌────┴─────┐        │
         │ React :5173 │ │ Django   │        │
         │ (Frontend)  │ │ :8000    │        │
         └─────────────┘ │ (API)    │        │
                         └────┬─────┘        │
                              │              │
                   ┌──────────┼──────────┐   │
                   │          │          │   │
            ┌──────┴───┐ ┌───┴───┐ ┌────┴───────┐
            │ Postgres │ │ Redis │ │ ML Service  │
            │ :5432    │ │ :6379 │ │ :8001       │
            └──────────┘ └───┬───┘ └─────────────┘
                             │
                      ┌──────┴──────┐
                      │   Celery    │
                      │   Workers   │
                      └──────┬──────┘
                             │
                      ┌──────┴──────┐
                      │    Data     │
                      │  Pipeline   │
                      └─────────────┘
```

## Services

### Backend (Django + DRF)
REST API server handling authentication, CRUD operations for campaigns, data sources, analytics metrics, and reports. Uses JWT for authentication and Celery for async task processing.

### Frontend (React + Vite)
Single-page application with dashboard, campaign management, report viewing, and data source configuration. Uses React Router for navigation, Zustand for state management, and React Query for server state.

### ML Services (FastAPI)
Microservice providing ML inference endpoints for sentiment analysis, campaign performance prediction, and anomaly detection. Designed to be independently scalable.

### Data Pipeline (Celery Workers)
Background workers that sync data from external ad platforms (Google Ads, Meta Ads, Google Analytics) into the platform's database. Uses pluggable connector architecture.

### Infrastructure
- **PostgreSQL** — Primary data store
- **Redis** — Celery broker/backend and caching
- **Nginx** — Reverse proxy routing API and frontend traffic

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/v1/auth/token/` | POST | Obtain JWT token |
| `/api/v1/auth/token/refresh/` | POST | Refresh JWT token |
| `/api/v1/users/` | CRUD | User management |
| `/api/v1/campaigns/` | CRUD | Campaign management |
| `/api/v1/data-sources/` | CRUD | Data source management |
| `/api/v1/analytics/metrics/` | CRUD | Metric snapshots |
| `/api/v1/analytics/metrics/summary/` | GET | Aggregated metrics |
| `/api/v1/reports/` | CRUD | Report management |
| `/api/v1/reports/{id}/generate/` | POST | Trigger report generation |

## Getting Started

```bash
# 1. Clone and configure
cp .env.example .env

# 2. Start all services
docker compose up --build

# 3. Run migrations
docker compose exec backend python manage.py migrate

# 4. Create admin user
docker compose exec backend python manage.py createsuperuser

# 5. Access the app
# Frontend: http://localhost:5173
# API: http://localhost:8000/api/v1/
# Admin: http://localhost:8000/admin/
# ML Docs: http://localhost:8001/docs
```
