from fastapi import APIRouter

from app.schemas.sentiment import SentimentRequest, SentimentResponse
from app.services.sentiment_service import analyze_sentiment

router = APIRouter()


@router.post("/analyze", response_model=SentimentResponse)
def analyze(request: SentimentRequest):
    result = analyze_sentiment(request.text)
    return result
