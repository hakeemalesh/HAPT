"""
Tests for MarketData caching behavior.
"""

from data.storage import DataStorage


def test_cache_exists_returns_false_for_missing_file(tmp_path):
    """
   A symbol that has never been downloaded should not have a cache.
    """
    storage = DataStorage(base_path=tmp_path)

    assert storage.cache_exists("SPY") is False