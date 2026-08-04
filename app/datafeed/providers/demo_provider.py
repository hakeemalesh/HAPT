"""
HAPT Demo Market Data Provider
------------------------------

Provides simulated market prices for testing
and development.
"""

from app.datafeed.providers.base_provider import BaseProvider


class DemoProvider(BaseProvider):
    """
    Demo market data provider.
    """

    def __init__(self):
        self._prices = {
            "MES": 6250.25,
            "MNQ": 23250.50,
            "M2K": 2250.75,
            "MYM": 45125.00,
            "ES": 6252.50,
            "NQ": 23260.25,
            "RTY": 2254.00,
            "YM": 45140.00,
            "CL": 68.45,
            "GC": 3445.60,
        }

    def get_provider_name(self) -> str:
        return "Demo Provider"

    def get_price(self, symbol: str):
        return self._prices.get(symbol)

    def symbol_exists(self, symbol: str) -> bool:
        return symbol in self._prices

    def get_all_prices(self) -> dict:
        return self._prices.copy()
