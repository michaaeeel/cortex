from abc import ABC, abstractmethod


class BaseConnector(ABC):
    def __init__(self, credentials: dict):
        self.credentials = credentials

    @abstractmethod
    def connect(self):
        """Establish connection to the data source."""

    @abstractmethod
    def fetch_data(self, start_date: str, end_date: str) -> list[dict]:
        """Fetch raw data from the source for the given date range."""

    @abstractmethod
    def transform(self, raw_data: list[dict]) -> list[dict]:
        """Transform raw data into the standard MetricSnapshot format."""
