"""
HAPT Market Data
----------------

Provides market data to HAPT.

This module is responsible for:
- Returning market prices
- Identifying the data provider
- Preparing for future live data connections
"""


class MarketData:
    """Supplies market prices and market information."""

    def __init__(self):
        """Initialize the market data provider."""

        self.provider = "Demo Data"

        self.demo_prices = {
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

    def get_price(self, symbol):
        """
        Return the latest available price for a symbol.
        """

        return self.demo_prices.get(symbol, 0.0)

    def get_provider(self):
        """
        Return the current market data provider.
        """

        return self.provider

    def symbol_exists(self, symbol):
        """
        Check whether a symbol exists.
        """

        return symbol in self.demo_prices

    def get_all_prices(self):
        """
        Return every available demo price.
        """

        return self.demo_prices.copy()