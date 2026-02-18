import logging

from fastapi import APIRouter, HTTPException

from app.schemas.insights import (
    CampaignInsightsRequest,
    DashboardInsightsRequest,
    InsightsResponse,
)
from app.services.llm_service import generate_campaign_summary, generate_dashboard_summary

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/campaign", response_model=InsightsResponse)
def campaign_insights(request: CampaignInsightsRequest):
    try:
        summary = generate_campaign_summary(request.model_dump())
        return {"summary": summary}
    except ValueError as e:
        raise HTTPException(status_code=503, detail=str(e))
    except Exception as e:
        logger.error("Failed to generate campaign insights: %s", e)
        raise HTTPException(status_code=500, detail="Failed to generate insights")


@router.post("/dashboard", response_model=InsightsResponse)
def dashboard_insights(request: DashboardInsightsRequest):
    try:
        summary = generate_dashboard_summary(request.model_dump())
        return {"summary": summary}
    except ValueError as e:
        raise HTTPException(status_code=503, detail=str(e))
    except Exception as e:
        logger.error("Failed to generate dashboard insights: %s", e)
        raise HTTPException(status_code=500, detail="Failed to generate insights")
