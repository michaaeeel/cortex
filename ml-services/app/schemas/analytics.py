from pydantic import BaseModel


class TrendInfo(BaseModel):
    direction: str  # "up", "down", "neutral"
    change_pct: float


class PeriodMetrics(BaseModel):
    impressions: int = 0
    clicks: int = 0
    conversions: int = 0
    spend: float = 0.0
    revenue: float = 0.0


class AnalyticsRequest(BaseModel):
    current_period: PeriodMetrics
    previous_period: PeriodMetrics | None = None


class AnalyticsResponse(BaseModel):
    impressions: int
    clicks: int
    conversions: int
    spend: float
    revenue: float
    ctr: float | None
    cpa: float | None
    roas: float | None
    cpc: float | None
    conversion_rate: float | None
    trends: dict | None
