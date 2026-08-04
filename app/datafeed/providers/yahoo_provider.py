"""
HAPT Yahoo Finance Provider
---------------------------

Market data provider backed by Yahoo Finance.
"""

import yfinance as yf

from app.datafeed.providers.base_provider import BaseProvider


class YahooProvider(BaseProvider):
    """
    Yahoo Finance market data provider.
    """

    def get_provider_name(self) -> str:
        return "Yahoo Finance"

    def get_price(self, symbol: str):
        ticker = yf.Ticker(symbol)
        history = ticker.history(period="1d")

        if history.empty:
            return None

        return float(history["Close"].iloc[-1])

    def symbol_exists(self, symbol: str) -> bool:
        return self.get_price(symbol) is not None

    def get_all_prices(self) -> dict:
        raise NotImplementedError(
            "YahooProvider does not support bulk price retrieval."
        )
