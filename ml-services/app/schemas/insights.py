from pydantic import BaseModel


class CampaignInsightsRequest(BaseModel):
    campaign_name: str = ""
    platform: str = ""
    status: str = ""
    impressions: int = 0
    clicks: int = 0
    conversions: int = 0
    spend: float = 0.0
    revenue: float = 0.0
    ctr: float | None = None
    cpa: float | None = None
    roas: float | None = None
    cpc: float | None = None
    trends: dict | None = None


class DashboardInsightsRequest(BaseModel):
    active_campaigns: int = 0
    total_campaigns: int = 0
    impressions: int = 0
    clicks: int = 0
    conversions: int = 0
    spend: float = 0.0
    revenue: float = 0.0
    ctr: float | None = None
    roas: float | None = None
    cpa: float | None = None
    period_days: int = 30
    trends: dict | None = None


class InsightsResponse(BaseModel):
    summary: str
