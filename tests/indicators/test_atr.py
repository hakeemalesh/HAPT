"""
HAPT ATR Tests
--------------

Unit tests for ATR calculations.
"""

import unittest

from app.indicators.atr import ATR


class TestATR(unittest.TestCase):
    """Tests for ATR."""

    def test_empty_input(self):
        """ATR should return None for empty inputs."""

        self.assertIsNone(
            ATR.calculate([], [], [])
        )

    def test_single_candle(self):
        """ATR for a single candle."""

        highs = [105]
        lows = [100]
        closes = [103]

        self.assertEqual(
            ATR.calculate(
                highs,
                lows,
                closes
            ),
            5.0
        )

    def test_multiple_candles(self):
        """ATR for multiple candles."""

        highs = [105, 108, 110]
        lows = [100, 103, 106]
        closes = [103, 107, 108]

        result = ATR.calculate(
            highs,
            lows,
            closes
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, float)
        self.assertGreater(result, 0)


if __name__ == "__main__":
    unittest.main()