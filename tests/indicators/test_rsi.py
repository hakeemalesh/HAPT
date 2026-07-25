"""
HAPT RSI Tests
--------------

Unit tests for RSI calculations.
"""

import unittest

from app.indicators.rsi import RSI


class TestRSI(unittest.TestCase):
    """Tests for RSI."""

    def test_empty_input(self):
        """RSI should return None for empty input."""

        self.assertIsNone(
            RSI.calculate([])
        )

    def test_single_price(self):
        """RSI should return None for insufficient data."""

        self.assertIsNone(
            RSI.calculate([100])
        )

    def test_rsi_range(self):
        """RSI should always be between 0 and 100."""

        prices = [
            100,
            101,
            102,
            101,
            103,
            104,
            102,
            105,
            106,
            107,
            106,
            108,
            109,
            110,
            111
        ]

        result = RSI.calculate(prices)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, float)
        self.assertGreaterEqual(result, 0)
        self.assertLessEqual(result, 100)


if __name__ == "__main__":
    unittest.main()