"""
Integration tests for the HAPT storage layer.
"""

import pandas as pd
from pandas.testing import assert_frame_equal

from data.storage import DataStorage


def test_save_and_load_csv(tmp_path):
    """
    Verify that data can be saved and loaded correctly.
    """
    storage = DataStorage()

    data = pd.DataFrame(
        {
            "Open": [100.0, 101.0],
            "High": [101.0, 102.0],
            "Low": [99.0, 100.0],
            "Close": [100.5, 101.5],
            "Volume": [1000, 1200],
        },
        index=pd.to_datetime(
            ["2025-01-01", "2025-01-02"]
        ),
    )

    filepath = tmp_path / "historical" / "SPY.csv"

    storage.save_csv(data, filepath)

    assert filepath.exists()

    loaded = storage.load_csv(filepath)

    assert_frame_equal(data, loaded)
