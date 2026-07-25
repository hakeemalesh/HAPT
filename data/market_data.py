"""
HAPT Market Data Engine

Provides a unified interface for retrieving market data
through interchangeable providers.
"""

from datetime import timedelta

from data.providers.base_provider import BaseProvider
from data.storage import DataStorage


class MarketData:
    """
    Core market data interface for HAPT.
    """

    def __init__(self, provider: BaseProvider):
        self.provider = provider
        self.storage = DataStorage()

    def get_historical_data(self, symbol: str, **kwargs):
        """
        Retrieve historical market data.

        If a fresh cache exists, load it from disk.
        Otherwise, download new data, update the cache,
        and return the downloaded data.
        """
        filepath = self.storage.historical_path(symbol)

        if (
            self.storage.cache_exists(symbol)
            and not self.storage.is_cache_stale(
                symbol,
                max_age=timedelta(days=1),
            )
        ):
            return self.storage.load_csv(filepath)

        data = self.provider.get_historical_data(symbol, **kwargs)

        self.storage.save_csv(data, filepath)

        return data

    def get_live_data(self, symbol: str, **kwargs):
        """
        Retrieve live market data from the configured provider.
        """
        return self.provider.get_live_data(symbol, **kwargs)