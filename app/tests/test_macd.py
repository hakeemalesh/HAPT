"""
HAPT MACD Tests
---------------

Unit tests for MACD calculations.
"""

import unittest

from indicators.macd import MACD


class TestMACD(unittest.TestCase):
    """Tests for MACD."""

    def test_empty_input(self):
        """MACD should return None for empty input."""

        self.assertIsNone(
            MACD.calculate([])
        )

    def test_single_price(self):
        """MACD should handle a single price."""

        result = MACD.calculate([100])

        self.assertIsNotNone(result)
        self.assertIn("ema_12", result)
        self.assertIn("ema_26", result)
        self.assertIn("macd", result)

    def test_multiple_prices(self):
        """MACD should return expected structure."""

        prices = list(range(1, 60))

        result = MACD.calculate(prices)

        self.assertIsInstance(result, dict)

        self.assertIn("ema_12", result)
        self.assertIn("ema_26", result)
        self.assertIn("macd", result)

        self.assertIsInstance(
            result["macd"],
            float
        )


if __name__ == "__main__":
    unittest.main()