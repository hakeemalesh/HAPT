"""
Yahoo Finance market data provider for HAPT.
"""

import yfinance as yf

from data.providers.base_provider import BaseProvider


class YahooFinanceProvider(BaseProvider):
    """
    Market data provider backed by Yahoo Finance.
    """

    def get_historical_data(
        self,
        symbol: str,
        period: str = "6mo",
        interval: str = "1d",
        **kwargs,
    ):
        """
        Download historical market data.
        """
        ticker = yf.Ticker(symbol)
        return ticker.history(
            period=period,
            interval=interval,
            **kwargs,
        )

    def get_live_data(self, symbol: str, **kwargs):
        """
        Retrieve the latest available market data.
        """
        ticker = yf.Ticker(symbol)
        data = ticker.history(period="1d", interval="1m")

        if data.empty:
            return None

        return data.iloc[-1]

    def save_data(self, symbol: str, data):
        raise NotImplementedError(
            "Saving data is handled by the storage layer."
        )

    def load_data(self, symbol: str):
        raise NotImplementedError(
            "Loading data is handled by the storage layer."
        )
