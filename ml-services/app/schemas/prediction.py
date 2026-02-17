from pydantic import BaseModel


class PredictionRequest(BaseModel):
    campaign_id: int
    features: dict


class PredictionResponse(BaseModel):
    predicted_roas: float
    confidence: float
