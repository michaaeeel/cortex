"""
Event simulator that generates fake real-time campaign events
and pushes them to a Redis Stream for consumption.
"""
import json
import logging
import os
import random
import time
from datetime import datetime, timezone

import redis

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

REDIS_URL = os.environ.get("REDIS_URL", "redis://redis:6379/0")
STREAM_KEY = "campaign_events"
INTERVAL = float(os.environ.get("SIMULATOR_INTERVAL", "2"))

# Simulated campaign IDs (these should match DB records)
CAMPAIGN_IDS = list(range(1, 6))

EVENT_TYPES = [
    {"type": "impression", "min": 50, "max": 500},
    {"type": "click", "min": 1, "max": 30},
    {"type": "conversion", "min": 0, "max": 5},
    {"type": "spend", "min": 0.5, "max": 25.0},
    {"type": "revenue", "min": 0.0, "max": 100.0},
]


def create_event(campaign_id: int) -> dict:
    """Generate a batch of metric events for a campaign."""
    return {
        "campaign_id": str(campaign_id),
        "impressions": str(random.randint(50, 500)),
        "clicks": str(random.randint(1, 30)),
        "conversions": str(random.randint(0, 5)),
        "spend": str(round(random.uniform(0.5, 25.0), 2)),
        "revenue": str(round(random.uniform(0.0, 100.0), 2)),
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


def main():
    logger.info("Connecting to Redis at %s", REDIS_URL)
    r = redis.from_url(REDIS_URL)
    r.ping()
    logger.info("Connected. Streaming events every %.1fs for campaigns %s", INTERVAL, CAMPAIGN_IDS)

    while True:
        campaign_id = random.choice(CAMPAIGN_IDS)
        event = create_event(campaign_id)

        r.xadd(STREAM_KEY, event, maxlen=10000)
        logger.info(
            "Event: campaign=%s imp=%s clicks=%s conv=%s spend=$%s rev=$%s",
            event["campaign_id"],
            event["impressions"],
            event["clicks"],
            event["conversions"],
            event["spend"],
            event["revenue"],
        )

        time.sleep(INTERVAL)


if __name__ == "__main__":
    main()
