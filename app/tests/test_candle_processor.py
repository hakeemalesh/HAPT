"""
HAPT Candle Processor Tests
---------------------------

Unit tests for CandleProcessor.
"""

import unittest

from processing.candle_processor import CandleProcessor


class TestCandleProcessor(unittest.TestCase):
    """Tests for CandleProcessor."""

    def test_empty_input(self):
        """Empty candle list should return empty series."""

        result = CandleProcessor.extract([])

        self.assertEqual(result["timestamps"], [])
        self.assertEqual(result["opens"], [])
        self.assertEqual(result["highs"], [])
        self.assertEqual(result["lows"], [])
        self.assertEqual(result["closes"], [])
        self.assertEqual(result["volumes"], [])

    def test_extract_single_candle(self):
        """Extract one candle correctly."""

        candles = [
            {
                "timestamp": "2026-07-22 09:30",
                "open": 100,
                "high": 105,
                "low": 99,
                "close": 103,
                "volume": 1200,
            }
        ]

        result = CandleProcessor.extract(candles)

        self.assertEqual(result["timestamps"], ["2026-07-22 09:30"])
        self.assertEqual(result["opens"], [100])
        self.assertEqual(result["highs"], [105])
        self.assertEqual(result["lows"], [99])
        self.assertEqual(result["closes"], [103])
        self.assertEqual(result["volumes"], [1200])

    def test_extract_multiple_candles(self):
        """Extract multiple candles correctly."""

        candles = [
            {
                "timestamp": "T1",
                "open": 10,
                "high": 12,
                "low": 9,
                "close": 11,
                "volume": 100,
            },
            {
                "timestamp": "T2",
                "open": 11,
                "high": 13,
                "low": 10,
                "close": 12,
                "volume": 150,
            },
        ]

        result = CandleProcessor.extract(candles)

        self.assertEqual(result["timestamps"], ["T1", "T2"])
        self.assertEqual(result["opens"], [10, 11])
        self.assertEqual(result["highs"], [12, 13])
        self.assertEqual(result["lows"], [9, 10])
        self.assertEqual(result["closes"], [11, 12])
        self.assertEqual(result["volumes"], [100, 150])


if __name__ == "__main__":
    unittest.main()