from fastapi import APIRouter

from app.schemas.analytics import AnalyticsRequest, AnalyticsResponse
from app.services.analytics_service import compute_campaign_analytics

router = APIRouter()


@router.post("/compute", response_model=AnalyticsResponse)
def compute_analytics(request: AnalyticsRequest):
    current = request.current_period.model_dump()
    previous = request.previous_period.model_dump() if request.previous_period else None
    result = compute_campaign_analytics(current, previous)
    return result
