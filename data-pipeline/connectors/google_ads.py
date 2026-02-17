from .base import BaseConnector


class GoogleAdsConnector(BaseConnector):
    def connect(self):
        # TODO: Initialize Google Ads API client
        pass

    def fetch_data(self, start_date: str, end_date: str) -> list[dict]:
        # TODO: Query Google Ads API
        return []

    def transform(self, raw_data: list[dict]) -> list[dict]:
        # TODO: Map Google Ads fields to MetricSnapshot format
        return []
