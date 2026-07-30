"""
HAPT Opportunity Engine Tests
-----------------------------

Unit tests for Opportunity Engine scoring.
"""

import unittest

from app.opportunity.opportunity_engine import OpportunityEngine
from app.rules.trading_rules import TradingRules


class TestOpportunityEngine(unittest.TestCase):
    """Tests for Opportunity Engine."""

    def setUp(self):
        """Create a fresh engine for every test."""

        self.engine = OpportunityEngine()

    def test_returns_dictionary(self):
        """Score should return a dictionary."""

        result = self.engine.score({})

        self.assertIsInstance(result, dict)

    def test_contains_required_keys(self):
        """Result should contain all required fields."""

        result = self.engine.score({})

        self.assertIn("overall", result)
        self.assertIn("trend", result)
        self.assertIn("momentum", result)
        self.assertIn("volume", result)
        self.assertIn("atr", result)
        self.assertIn("vwap", result)
        self.assertIn("session", result)
        self.assertIn("grade", result)

    def test_grade_is_string(self):
        """Grade should always be a string."""

        result = self.engine.score({})

        self.assertIsInstance(
            result["grade"],
            str
        )

    def test_overall_is_integer(self):
        """Overall score should be an integer."""

        result = self.engine.score({})

        self.assertIsInstance(
            result["overall"],
            int
        )

    def test_empty_context(self):
        """Engine should not fail with an empty context."""

        result = self.engine.score({})

        self.assertIsNotNone(result)

    def test_missing_values(self):
        """Engine should safely handle missing fields."""

        context = {
            "ema_9": None,
            "ema_20": None,
            "ema_50": None,
            "ema_200": None,
        }

        result = self.engine.score(context)

        self.assertIsInstance(
            result,
            dict
        )

    def test_bullish_trend_score(self):
        """Bullish EMA alignment should award trend points."""

        context = {
            "ema_9": 105,
            "ema_20": 104,
            "ema_50": 103,
            "ema_200": 100,
        }

        result = self.engine.score(context)

        self.assertEqual(
            result["trend"],
            TradingRules.EMA_ALIGNMENT_SCORE
        )

    def test_bearish_trend_score(self):
        """Bearish EMA alignment should award trend points."""

        context = {
            "ema_9": 100,
            "ema_20": 101,
            "ema_50": 102,
            "ema_200": 103,
        }

        result = self.engine.score(context)

        self.assertEqual(
            result["trend"],
            TradingRules.EMA_ALIGNMENT_SCORE
        )

    def test_sideways_trend_score(self):
        """Sideways EMA alignment should score zero."""

        context = {
            "ema_9": 102,
            "ema_20": 101,
            "ema_50": 103,
            "ema_200": 100,
        }

        result = self.engine.score(context)

        self.assertEqual(
            result["trend"],
            0
        )

    def test_high_relative_volume(self):
        """High relative volume should award volume points."""

        context = {
            "relative_volume":
                TradingRules.RELATIVE_VOLUME_HIGH
        }

        result = self.engine.score(context)

        self.assertEqual(
            result["volume"],
            TradingRules.RELATIVE_VOLUME_SCORE
        )

    def test_bullish_rsi(self):
        """Bullish RSI should award momentum points."""

        context = {
            "rsi": TradingRules.RSI_BULLISH
        }

        result = self.engine.score(context)

        self.assertEqual(
            result["momentum"],
            TradingRules.RSI_SCORE
        )

    def test_macd_score(self):
        """MACD should award momentum points."""

        context = {
            "macd": 0.75
        }

        result = self.engine.score(context)

        self.assertEqual(
            result["momentum"],
            TradingRules.MACD_SCORE
        )

    def test_poor_atr_score(self):
        """Missing ATR should score zero."""

        result = self.engine.score({})

        self.assertEqual(
            result["atr"],
            TradingRules.ATR_POOR_SCORE
        )

    def test_fair_atr_score(self):
        """Fair ATR should award fair points."""

        context = {
            "atr": TradingRules.ATR_FAIR_THRESHOLD
        }

        result = self.engine.score(context)

        self.assertEqual(
            result["atr"],
            TradingRules.ATR_FAIR_SCORE
        )

    def test_good_atr_score(self):
        """Good ATR should award maximum ATR points."""

        context = {
            "atr": TradingRules.ATR_GOOD_THRESHOLD
        }

        result = self.engine.score(context)

        self.assertEqual(
            result["atr"],
            TradingRules.ATR_GOOD_SCORE
        )

    def test_missing_vwap_score(self):
        """Missing VWAP data should score zero."""

        result = self.engine.score({})

        self.assertEqual(
            result["vwap"],
            TradingRules.VWAP_POOR_SCORE
        )

    def test_price_above_vwap(self):
        """Price above VWAP should award VWAP points."""

        context = {
            "price": 101.0,
            "vwap": 100.0,
        }

        result = self.engine.score(context)

        self.assertEqual(
            result["vwap"],
            TradingRules.VWAP_GOOD_SCORE
        )

    def test_price_equal_vwap(self):
        """Price equal to VWAP should award VWAP points."""

        context = {
            "price": 100.0,
            "vwap": 100.0,
        }

        result = self.engine.score(context)

        self.assertEqual(
            result["vwap"],
            TradingRules.VWAP_GOOD_SCORE
        )

    def test_price_below_vwap(self):
        """Price below VWAP should score zero."""

        context = {
            "price": 99.0,
            "vwap": 100.0,
        }

        result = self.engine.score(context)

        self.assertEqual(
            result["vwap"],
            TradingRules.VWAP_POOR_SCORE
        )


if __name__ == "__main__":
    unittest.main()