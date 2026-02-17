from fastapi import APIRouter

from app.schemas.anomaly import AnomalyRequest, AnomalyResponse
from app.services.anomaly_service import detect_anomalies

router = APIRouter()


@router.post("/detect", response_model=AnomalyResponse)
def detect(request: AnomalyRequest):
    anomalies = detect_anomalies(request.metric_values)
    return {"anomalies": anomalies}
