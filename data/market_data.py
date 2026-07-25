"""
HAPT Market Data Engine

Provides a unified interface for retrieving market data
through interchangeable providers.
"""

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

        If cached data exists, load it from disk.
        Otherwise, download it, save it to the cache,
        and return the downloaded data.
        """
        filepath = self.storage.historical_path(symbol)

        if self.storage.cache_exists(symbol):
            return self.storage.load_csv(filepath)

        data = self.provider.get_historical_data(symbol, **kwargs)

        self.storage.save_csv(data, filepath)

        return data

    def get_live_data(self, symbol: str, **kwargs):
        """
        Retrieve live market data from the configured provider.
        """
        return self.provider.get_live_data(symbol, **kwargs)