from pydantic import BaseModel


class AnomalyRequest(BaseModel):
    metric_values: list[float]


class AnomalyItem(BaseModel):
    index: int
    value: float
    z_score: float


class AnomalyResponse(BaseModel):
    anomalies: list[AnomalyItem]
