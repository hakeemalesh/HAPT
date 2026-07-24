"""
HAPT Market Data
----------------

Central access point for market data.

This module coordinates:
- Data Provider
- Historical Data
- Demo Historical Data

Other HAPT modules should interact with this class rather
than individual data sources.
"""


from datafeed.demo_historical_data import DemoHistoricalData
from datafeed.data_provider import DataProvider
from datafeed.historical_data import HistoricalData


class MarketData:
    """Provides access to market data."""

    def __init__(self, provider="demo"):
        """Initialize the market data system."""

        self.provider = DataProvider(provider)

        self.history = HistoricalData()

        self.demo_history = DemoHistoricalData()

        self.load_demo_history()


    # --------------------------------------------------
    # Provider Information
    # --------------------------------------------------

    def get_provider(self):
        """Return the active provider."""

        return self.provider.get_provider_name()


    # --------------------------------------------------
    # Live / Current Price
    # --------------------------------------------------

    def get_price(self, symbol):
        """Return the latest price."""

        return self.provider.get_price(symbol)


    def symbol_exists(self, symbol):
        """Return True if the symbol exists."""

        return self.provider.symbol_exists(symbol)


    def get_all_prices(self):
        """Return all available prices."""

        return self.provider.get_all_prices()


    # --------------------------------------------------
    # Historical Data
    # --------------------------------------------------

    def add_historical_data(self, symbol, timeframe, candles):
        """Store historical candle data."""

        self.history.add_candles(
            symbol,
            timeframe,
            candles
        )


    def get_historical_data(self, symbol, timeframe="5m"):
        """Return historical candle data."""

        return self.history.get_candles(
            symbol,
            timeframe
        )


    def has_historical_data(self, symbol, timeframe="5m"):
        """Return True if historical data exists."""

        return self.history.has_data(
            symbol,
            timeframe
        )


    # --------------------------------------------------
    # Demo Historical Data
    # --------------------------------------------------

    def load_demo_history(self):
        """
        Load demo historical candles.
        """

        symbols = [
            "MES",
            "MNQ",
            "M2K",
            "MYM",
            "ES",
            "NQ",
            "RTY",
            "YM",
            "CL",
            "GC"
        ]


        for symbol in symbols:

            candles = self.demo_history.generate(symbol)

            self.add_historical_data(
                symbol,
                "5m",
                candles
            )


    # --------------------------------------------------
    # Maintenance
    # --------------------------------------------------

    def clear_history(self):
        """Clear all historical data."""

        self.history.clear()