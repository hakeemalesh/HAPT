"""
Integration tests for the HAPT MarketData class.
"""

import pandas as pd

from data.market_data import MarketData
from data.providers.yahoo_provider import YahooFinanceProvider


def test_market_data_download():
    """
    Verify that MarketData downloads historical data.
    """
    provider = YahooFinanceProvider()
    market_data = MarketData(provider)

    data = market_data.get_historical_data(
        symbol="SPY",
        period="1mo",
        interval="1d",
    )

    assert isinstance(data, pd.DataFrame)
    assert not data.empty

    expected_columns = [
        "Open",
        "High",
        "Low",
        "Close",
        "Volume",
    ]

    for column in expected_columns:
        assert column in data.columns
