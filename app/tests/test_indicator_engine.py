"""
HAPT Indicator Engine Tests
---------------------------

Unit tests for IndicatorEngine.
"""

import unittest

from indicators.indicator_engine import IndicatorEngine


class TestIndicatorEngine(unittest.TestCase):
    """Tests for IndicatorEngine."""

    def test_empty_input(self):
        """IndicatorEngine should handle empty input."""

        result = IndicatorEngine.calculate(
            closes=[],
            highs=[],
            lows=[],
            volumes=[]
        )

        self.assertIsInstance(result, dict)

        self.assertIn("ema", result)
        self.assertIn("rsi", result)
        self.assertIn("macd", result)
        self.assertIn("atr", result)
        self.assertIn("vwap", result)
        self.assertIn("volume", result)

    def test_valid_input(self):
        """IndicatorEngine should return all indicators."""

        closes = list(range(100, 130))
        highs = [price + 1 for price in closes]
        lows = [price - 1 for price in closes]
        volumes = [1000] * len(closes)

        result = IndicatorEngine.calculate(
            closes=closes,
            highs=highs,
            lows=lows,
            volumes=volumes
        )

        self.assertIsInstance(result, dict)

        self.assertIn("ema", result)
        self.assertIn("rsi", result)
        self.assertIn("macd", result)
        self.assertIn("atr", result)
        self.assertIn("vwap", result)
        self.assertIn("volume", result)

        self.assertIsInstance(result["ema"], dict)
        self.assertIsInstance(result["macd"], dict)
        self.assertIsInstance(result["volume"], dict)


if __name__ == "__main__":
    unittest.main()