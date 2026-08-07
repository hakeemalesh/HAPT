"""
HAPT Market Data
----------------

Central gateway for all HAPT market data.

Responsibilities
----------------
- Live market prices
- Historical market data
- Provider management
- Historical data storage

This class isolates the rest of HAPT from
individual market data providers.
"""

from app.datafeed.demo_historical_data import (
    DemoHistoricalData,
)
from app.datafeed.historical_data import (
    HistoricalData,
)
from app.datafeed.providers.provider_factory import (
    ProviderFactory,
)
from app.datafeed.yahoo_historical_data import (
    YahooHistoricalData,
)


class MarketData:
    """
    Central market data interface used by HAPT.
    """

    #
    # Internal HAPT → Yahoo symbol mapping
    #
    YAHOO_SYMBOLS = {
        "MES": "MES=F",
        "MNQ": "MNQ=F",
        "M2K": "M2K=F",
        "MYM": "MYM=F",
        "ES": "ES=F",
        "NQ": "NQ=F",
        "RTY": "RTY=F",
        "YM": "YM=F",
        "CL": "CL=F",
        "GC": "GC=F",
    }

    DEFAULT_SYMBOLS = [
        "MES",
        "MNQ",
        "M2K",
        "MYM",
        "ES",
        "NQ",
        "RTY",
        "YM",
        "CL",
        "GC",
    ]

    def __init__(self, provider="demo"):
        """
        Initialize the market data system.
        """

        self.provider_name = provider.lower()

        self.provider = ProviderFactory.create(
            self.provider_name
        )

        self.history = HistoricalData()

        self.demo_history = DemoHistoricalData()

        self.yahoo_history = YahooHistoricalData()

        if self.provider_name == "demo":

            self.load_demo_history()

        elif self.provider_name == "yahoo":

            self.load_yahoo_history()
    # --------------------------------------------------
    # Provider Information
    # --------------------------------------------------

    def get_provider(self):
        """
        Return the active provider name.
        """

        return self.provider.get_provider_name()

    # --------------------------------------------------
    # Symbol Translation
    # --------------------------------------------------

    def _provider_symbol(self, symbol):
        """
        Translate internal HAPT symbols into
        provider-specific symbols.
        """

        if self.provider_name == "yahoo":

            return self.YAHOO_SYMBOLS.get(
                symbol,
                symbol,
            )

        return symbol

    # --------------------------------------------------
    # Live Prices
    # --------------------------------------------------

    def get_price(self, symbol):
        """
        Return the latest market price.
        """

        provider_symbol = self._provider_symbol(
            symbol
        )

        return self.provider.get_price(
            provider_symbol
        )

    def symbol_exists(self, symbol):
        """
        Return True if the symbol exists.
        """

        provider_symbol = self._provider_symbol(
            symbol
        )

        return self.provider.symbol_exists(
            provider_symbol
        )

    def get_all_prices(self):
        """
        Return all available prices.

        Not every provider supports this
        operation.
        """

        return self.provider.get_all_prices()
    # --------------------------------------------------
    # Historical Data
    # --------------------------------------------------

    def add_historical_data(
        self,
        symbol,
        timeframe,
        candles,
    ):
        """
        Store historical candles.
        """

        self.history.add_candles(
            symbol,
            timeframe,
            candles,
        )

    def get_historical_data(
        self,
        symbol,
        timeframe="5m",
    ):
        """
        Return historical candles.
        """

        return self.history.get_candles(
            symbol,
            timeframe,
        )

    def has_historical_data(
        self,
        symbol,
        timeframe="5m",
    ):
        """
        Return True if historical data exists.
        """

        return self.history.has_data(
            symbol,
            timeframe,
        )

    # --------------------------------------------------
    # Historical Loaders
    # --------------------------------------------------

    def load_demo_history(self):
        """
        Load demo historical candles.
        """

        for symbol in self.DEFAULT_SYMBOLS:

            candles = self.demo_history.generate(
                symbol
            )

            self.add_historical_data(
                symbol,
                "5m",
                candles,
            )

    def load_yahoo_history(self):
        """
        Load Yahoo Finance historical candles.
        """

        for symbol in self.DEFAULT_SYMBOLS:

            provider_symbol = self._provider_symbol(
                symbol
            )

            candles = (
                self.yahoo_history.get_candles(
                    provider_symbol
                )
            )

            if candles:

                self.add_historical_data(
                    symbol,
                    "5m",
                    candles,
                )
