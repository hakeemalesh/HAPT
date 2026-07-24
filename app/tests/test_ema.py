"""
HAPT EMA Tests
--------------

Unit tests for EMA calculations.
"""

import unittest

from indicators.ema import EMA


class TestEMA(unittest.TestCase):
    """Tests for EMA."""

    def test_empty_input(self):
        """EMA should return None for empty input."""

        self.assertIsNone(
            EMA.calculate([], 9)
        )

    def test_single_price(self):
        """EMA of a single value should equal that value."""

        self.assertEqual(
            EMA.calculate([100], 9),
            100
        )

    def test_multiple_prices(self):
        """EMA should return a float for multiple prices."""

        prices = [
            100,
            101,
            102,
            103,
            104,
            105,
            106,
            107,
            108,
            109
        ]

        result = EMA.calculate(
            prices,
            9
        )

        self.assertIsNotNone(result)
        self.assertIsInstance(result, float)

    def test_calculate_all(self):
        """All EMA periods should be returned."""

        prices = list(range(1, 250))

        result = EMA.calculate_all(prices)

        self.assertIn("ema_9", result)
        self.assertIn("ema_20", result)
        self.assertIn("ema_50", result)
        self.assertIn("ema_200", result)

        self.assertIsInstance(
            result["ema_9"],
            float
        )


if __name__ == "__main__":
    unittest.main()