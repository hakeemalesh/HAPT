"""
Integration tests for the Yahoo Finance provider.
"""

import pandas as pd

from data.providers.yahoo_provider import YahooFinanceProvider


def test_get_historical_data():
    """
    Verify that Yahoo Finance returns historical data.
    """
    provider = YahooFinanceProvider()

    data = provider.get_historical_data(
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
