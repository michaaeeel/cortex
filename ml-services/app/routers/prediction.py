from fastapi import APIRouter

from app.schemas.prediction import PredictionRequest, PredictionResponse
from app.services.prediction_service import predict_campaign_performance

router = APIRouter()


@router.post("/campaign-performance", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    result = predict_campaign_performance(request.campaign_id, request.features)
    return result
