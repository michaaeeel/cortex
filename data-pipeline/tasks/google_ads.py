import logging

from celery import shared_task

logger = logging.getLogger(__name__)


@shared_task(bind=True, max_retries=3)
def sync_google_ads(self, data_source_id):
    """Sync data from Google Ads API."""
    logger.info("Syncing Google Ads data for source %s", data_source_id)
    # TODO: Implement Google Ads API integration
    return {"status": "completed", "data_source_id": data_source_id}
