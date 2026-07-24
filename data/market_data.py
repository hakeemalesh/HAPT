"""
HAPT Market Data Engine

Provides a unified interface for retrieving market data
through interchangeable providers.
"""

from pathlib import Path

from data.providers.base_provider import BaseProvider


class MarketData:
    """
    Core market data interface for HAPT.
    """

    def __init__(self, provider: BaseProvider):
        self.provider = provider

        self.base_path = Path("data")
        self.historical_path = self.base_path / "historical"
        self.live_path = self.base_path / "live"
        self.logs_path = self.base_path / "logs"

    def get_historical_data(self, symbol: str, **kwargs):
        """
        Retrieve historical market data from the configured provider.
        """
        return self.provider.get_historical_data(symbol, **kwargs)

    def get_live_data(self, symbol: str, **kwargs):
        """
        Retrieve live market data from the configured provider.
        """
        return self.provider.get_live_data(symbol, **kwargs)
