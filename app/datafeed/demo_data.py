"""
HAPT Demo Market Data
---------------------

Provides demo market prices for development and testing.
"""


class DemoData:
    """Supplies demo market prices."""

    def __init__(self):
        """Initialize demo prices."""

        self.prices = {
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
        """Return the latest demo price."""

        return self.prices.get(symbol)

    def symbol_exists(self, symbol):
        """Return True if the symbol exists."""

        return symbol in self.prices

    def get_all_prices(self):
        """Return a copy of all demo prices."""

        return self.prices.copy()