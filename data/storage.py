"""
Storage utilities for HAPT market data.
"""

from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd


class DataStorage:
    """
    Handles saving and loading market data.
    """

    def __init__(self, base_path: str = "data"):
        self.base_path = Path(base_path)

    def ensure_directory(self, directory: Path):
        """
        Create the directory if it does not already exist.
        """
        directory.mkdir(parents=True, exist_ok=True)

    def historical_path(self, symbol: str) -> Path:
        """
        Return the cache file path for historical data.
        """
        return self.base_path / "historical" / f"{symbol}.csv"

    def cache_exists(self, symbol: str) -> bool:
        """
        Return True if cached historical data exists.
        """
        return self.historical_path(symbol).exists()

    def cache_age(self, symbol: str) -> timedelta | None:
        """
        Return the age of the cached file.

        Returns None if the cache file does not exist.
        """
        filepath = self.historical_path(symbol)

        if not filepath.exists():
            return None

        modified = datetime.fromtimestamp(filepath.stat().st_mtime)

        return datetime.now() - modified

    def is_cache_stale(
        self,
        symbol: str,
        max_age: timedelta = timedelta(days=1),
    ) -> bool:
        """
        Return True if the cache is stale.

        Missing cache files are considered stale.
        """
        age = self.cache_age(symbol)

        if age is None:
            return True

        return age > max_age

    def save_csv(self, data: pd.DataFrame, filepath: Path):
        """
        Save a DataFrame as a CSV file.
        """
        self.ensure_directory(filepath.parent)
        data.to_csv(filepath)

    def load_csv(self, filepath: Path) -> pd.DataFrame:
        """
        Load a CSV file into a DataFrame.
        """
        return pd.read_csv(
            filepath,
            index_col=0,
            parse_dates=True,
        )