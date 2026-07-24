"""
HAPT VWAP Tests
---------------

Unit tests for VWAP calculations.
"""

import unittest

from indicators.vwap import VWAP


class TestVWAP(unittest.TestCase):
    """Tests for VWAP."""

    def test_empty_input(self):
        """VWAP should return None for empty inputs."""

        self.assertIsNone(
            VWAP.calculate([], [], [], [])
        )

    def test_single_candle(self):
        """VWAP for a single candle."""

        highs = [105]
        lows = [95]
        closes = [100]
        volumes = [1000]

        # Typical Price = (105 + 95 + 100) / 3 = 100
        self.assertEqual(
            VWAP.calculate(
                highs,
                lows,
                closes,
                volumes
            ),
            100.0
        )

    def test_multiple_candles(self):
        """VWAP for multiple candles."""

        highs = [105, 110]
        lows = [95, 100]
        closes = [100, 105]
        volumes = [1000, 2000]

        result = VWAP.calculate(
            highs,
            lows,
            closes,
            volumes
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, float)


if __name__ == "__main__":
    unittest.main()