"""
Management command that consumes events from Redis Stream,
updates MetricSnapshot records, and broadcasts live updates
via Django Channels.
"""
import json
import logging
from datetime import date

import redis
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.conf import settings
from django.core.management.base import BaseCommand

from analytics.models import MetricSnapshot

logger = logging.getLogger(__name__)

STREAM_KEY = "campaign_events"
GROUP_NAME = "cortex_consumers"
CONSUMER_NAME = "consumer_1"


class Command(BaseCommand):
    help = "Consume campaign events from Redis Stream and update metrics"

    def handle(self, *args, **options):
        redis_url = settings.CELERY_BROKER_URL
        r = redis.from_url(redis_url)
        channel_layer = get_channel_layer()

        # Create consumer group (ignore if exists)
        try:
            r.xgroup_create(STREAM_KEY, GROUP_NAME, id="0", mkstream=True)
            logger.info("Created consumer group '%s'", GROUP_NAME)
        except redis.ResponseError as e:
            if "BUSYGROUP" not in str(e):
                raise
            logger.info("Consumer group '%s' already exists", GROUP_NAME)

        logger.info("Listening for events on stream '%s'...", STREAM_KEY)

        while True:
            # Block for up to 5 seconds waiting for new events
            entries = r.xreadgroup(
                GROUP_NAME,
                CONSUMER_NAME,
                {STREAM_KEY: ">"},
                count=10,
                block=5000,
            )

            if not entries:
                continue

            for stream, messages in entries:
                for msg_id, data in messages:
                    try:
                        self._process_event(data, channel_layer)
                        r.xack(STREAM_KEY, GROUP_NAME, msg_id)
                    except Exception:
                        logger.exception("Failed to process event %s", msg_id)

    def _process_event(self, data: dict, channel_layer):
        """Process a single event: upsert MetricSnapshot and broadcast."""
        # Redis returns bytes
        campaign_id = int(data[b"campaign_id"])
        impressions = int(data[b"impressions"])
        clicks = int(data[b"clicks"])
        conversions = int(data[b"conversions"])
        spend = float(data[b"spend"])
        revenue = float(data[b"revenue"])
        today = date.today()

        snapshot, created = MetricSnapshot.objects.get_or_create(
            campaign_id=campaign_id,
            date=today,
            defaults={
                "impressions": 0,
                "clicks": 0,
                "conversions": 0,
                "spend": 0,
                "revenue": 0,
            },
        )

        snapshot.impressions += impressions
        snapshot.clicks += clicks
        snapshot.conversions += conversions
        snapshot.spend += spend
        snapshot.revenue += revenue
        snapshot.save()  # triggers CTR/ROAS computation in model.save()

        # Broadcast live update via Channels
        update = {
            "campaign_id": campaign_id,
            "date": str(today),
            "impressions": snapshot.impressions,
            "clicks": snapshot.clicks,
            "conversions": snapshot.conversions,
            "spend": float(snapshot.spend),
            "revenue": float(snapshot.revenue),
            "ctr": snapshot.ctr,
            "roas": snapshot.roas,
        }

        async_to_sync(channel_layer.group_send)(
            "live_metrics",
            {
                "type": "metrics_update",
                "data": update,
            },
        )

        logger.info(
            "Updated campaign %d: imp=%d clicks=%d conv=%d spend=%.2f rev=%.2f",
            campaign_id,
            snapshot.impressions,
            snapshot.clicks,
            snapshot.conversions,
            float(snapshot.spend),
            float(snapshot.revenue),
        )
