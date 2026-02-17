from fastapi import FastAPI

from app.routers import anomaly, health, prediction, sentiment

app = FastAPI(title="Cortex ML Services", version="0.1.0")

app.include_router(health.router, tags=["health"])
app.include_router(sentiment.router, prefix="/api/v1/sentiment", tags=["sentiment"])
app.include_router(prediction.router, prefix="/api/v1/prediction", tags=["prediction"])
app.include_router(anomaly.router, prefix="/api/v1/anomaly", tags=["anomaly"])
