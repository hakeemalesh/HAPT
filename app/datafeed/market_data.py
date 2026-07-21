"""
HAPT Market Data
----------------

Provides market data to HAPT.
"""


class MarketData:
    """Supplies market prices and basic information."""

    def __init__(self):
        self.provider = "Demo Data"

    def get_price(self, symbol):
        """Return the latest price."""

        demo_prices = {
            "MES": 6250.25,
            "MNQ": 23250.50,
        }

        return demo_prices.get(symbol, 0.0)

    def get_provider(self):
        """Return the active data provider."""

        return self.provider