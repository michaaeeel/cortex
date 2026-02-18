from fastapi import Depends, FastAPI, Header, HTTPException

from app.config import settings
from app.routers import analytics, anomaly, health, insights, prediction, sentiment


def verify_internal_key(x_internal_key: str = Header(default="")):
    """Verify the internal API key if one is configured."""
    if settings.internal_api_key and x_internal_key != settings.internal_api_key:
        raise HTTPException(status_code=403, detail="Invalid internal API key")


app = FastAPI(title="Cortex ML Services", version="0.1.0")

app.include_router(health.router, tags=["health"])
app.include_router(sentiment.router, prefix="/api/v1/sentiment", tags=["sentiment"], dependencies=[Depends(verify_internal_key)])
app.include_router(prediction.router, prefix="/api/v1/prediction", tags=["prediction"], dependencies=[Depends(verify_internal_key)])
app.include_router(anomaly.router, prefix="/api/v1/anomaly", tags=["anomaly"], dependencies=[Depends(verify_internal_key)])
app.include_router(analytics.router, prefix="/api/v1/analytics", tags=["analytics"], dependencies=[Depends(verify_internal_key)])
app.include_router(insights.router, prefix="/api/v1/insights", tags=["insights"], dependencies=[Depends(verify_internal_key)])
