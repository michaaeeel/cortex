import random


def analyze_sentiment(text: str) -> dict:
    """Placeholder sentiment analysis. Returns a random label and score."""
    labels = ["positive", "negative", "neutral"]
    label = random.choice(labels)
    score = round(random.uniform(0.5, 1.0), 3)
    return {"label": label, "score": score}
