"""
HAPT Data Provider
------------------

Selects the active market data source.
"""

from app.datafeed.demo_data import DemoData


class DataProvider:
    """Provides access to the active market data source."""

    def __init__(self, provider="demo"):
        """Initialize the selected data provider."""

        self.provider = provider.lower()

        if self.provider == "demo":
            self.source = DemoData()
        else:
            raise ValueError(
                f"Unsupported data provider: {provider}"
            )

    def get_provider_name(self):
        """Return the active provider name."""

        return self.provider

    def get_price(self, symbol):
        """Return the latest available price."""

        return self.source.get_price(symbol)

    def symbol_exists(self, symbol):
        """Return True if the symbol exists."""

        return self.source.symbol_exists(symbol)

    def get_all_prices(self):
        """Return all available prices."""

        return self.source.get_all_prices()