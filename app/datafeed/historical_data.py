"""
HAPT Historical Market Data
---------------------------

Provides historical OHLCV candle data for development
and future live integrations.
"""


class HistoricalData:
    """Supplies historical candle data."""

    def __init__(self):
        """Initialize historical data."""

        self.provider = "Demo Historical Data"

        self.data = {}

    def get_provider(self):
        """Return the current data provider."""

        return self.provider

    def add_candles(self, symbol, timeframe, candles):
        """
        Store historical candles.

        Parameters
        ----------
        symbol : str
            Trading symbol (e.g. MES).
        timeframe : str
            Candle timeframe (e.g. 5m).
        candles : list
            List of OHLCV candle dictionaries.
        """

        if symbol not in self.data:
            self.data[symbol] = {}

        self.data[symbol][timeframe] = candles

    def get_candles(self, symbol, timeframe):
        """
        Return stored candles.
        """

        return (
            self.data
            .get(symbol, {})
            .get(timeframe, [])
        )

    def has_data(self, symbol, timeframe):
        """
        Return True if candles exist.
        """

        return (
            symbol in self.data
            and timeframe in self.data[symbol]
        )

    def clear(self):
        """
        Remove all stored historical data.
        """

        self.data.clear()