"""
HAPT VWAP Tests
---------------

Unit tests for VWAP calculations.
"""

import unittest

from app.indicators.vwap import VWAP


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
        """VWAP should return a float."""

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

    def test_mismatched_lengths(self):
        """Mismatched inputs should return None."""

        self.assertIsNone(
            VWAP.calculate(
                [100],
                [90],
                [95],
                []
            )
        )

    def test_zero_volume(self):
        """Zero total volume should return None."""

        self.assertIsNone(
            VWAP.calculate(
                [100],
                [90],
                [95],
                [0]
            )
        )

    def test_known_vwap(self):
        """Known VWAP calculation."""

        highs = [110, 120]
        lows = [90, 100]
        closes = [100, 110]
        volumes = [1000, 1000]

        # Candle 1 TP = 100
        # Candle 2 TP = 110
        # VWAP = (100000 + 110000) / 2000 = 105

        self.assertEqual(
            VWAP.calculate(
                highs,
                lows,
                closes,
                volumes
            ),
            105.0
        )


if __name__ == "__main__":
    unittest.main()