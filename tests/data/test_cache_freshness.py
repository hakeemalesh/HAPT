"""
Tests for cache freshness.
"""

from data.storage import DataStorage


def test_missing_cache_is_stale(tmp_path):
    """
    A missing cache file should always be considered stale.
    """
    storage = DataStorage(base_path=tmp_path)

    assert storage.is_cache_stale("SPY") is True