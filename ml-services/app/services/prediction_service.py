import random


def predict_campaign_performance(campaign_id: int, features: dict) -> dict:
    """Placeholder prediction. Returns mock ROAS prediction."""
    return {
        "predicted_roas": round(random.uniform(1.0, 5.0), 2),
        "confidence": round(random.uniform(0.6, 0.95), 2),
    }
