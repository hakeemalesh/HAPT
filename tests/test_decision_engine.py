"""
HAPT Decision Engine Tests
--------------------------

Unit tests for Decision Engine.
"""

import unittest

from app.decision.decision_engine import DecisionEngine
from app.models.decision import Decision


class TestDecisionEngine(unittest.TestCase):

    def setUp(self):
        self.engine = DecisionEngine()

    def test_returns_decision_object(self):
        context = {
            "market_open": False,
        }

        result = self.engine.evaluate(context)

        self.assertIsInstance(result, Decision)

    def test_market_closed_returns_wait(self):
        context = {
            "market_open": False,
        }

        result = self.engine.evaluate(context)

        self.assertEqual(result.signal, "WAIT")
        self.assertEqual(result.grade, "D")
        self.assertEqual(result.score, 0)

    def test_decision_contains_required_fields(self):
        context = {
            "market_open": False,
        }

        result = self.engine.evaluate(context)

        self.assertTrue(hasattr(result, "symbol"))
        self.assertTrue(hasattr(result, "market"))
        self.assertTrue(hasattr(result, "score"))
        self.assertTrue(hasattr(result, "confidence"))
        self.assertTrue(hasattr(result, "grade"))
        self.assertTrue(hasattr(result, "signal"))
        self.assertTrue(hasattr(result, "reasons"))
        self.assertTrue(hasattr(result, "details"))

    def test_grade_is_string(self):
        result = self.engine.evaluate(
            {"market_open": False}
        )

        self.assertIsInstance(result.grade, str)

    def test_signal_is_string(self):
        result = self.engine.evaluate(
            {"market_open": False}
        )

        self.assertIsInstance(result.signal, str)

    def test_reasons_is_list(self):
        result = self.engine.evaluate(
            {"market_open": False}
        )

        self.assertIsInstance(result.reasons, list)

    def test_details_is_dict(self):
        result = self.engine.evaluate(
            {"market_open": False}
        )

        self.assertIsInstance(result.details, dict)

    def test_confidence_is_numeric(self):
        result = self.engine.evaluate(
            {"market_open": False}
        )

        self.assertIsInstance(
            result.confidence,
            (int, float),
        )
    def test_buy_signal_for_a_plus_opportunity(self):
        context = {
            "market_open": True,
            "symbol": "MES",
            "market": "Futures",
            "opportunity": {
                "score": 95,
                "confidence": 95,
                "grade": "A+",
                "recommendation": "BUY",
                "reasons": ["Excellent confluence"],
            },
        }

        result = self.engine.evaluate(context)

        self.assertEqual(result.signal, "BUY")

    def test_watch_signal_for_b_opportunity(self):
        context = {
            "market_open": True,
            "symbol": "MES",
            "market": "Futures",
            "opportunity": {
                "score": 70,
                "confidence": 70,
                "grade": "B",
                "recommendation": "WATCH",
                "reasons": ["Average confluence"],
            },
        }

        result = self.engine.evaluate(context)

        self.assertEqual(result.signal, "WATCH")

    def test_wait_signal_for_d_opportunity(self):
        context = {
            "market_open": True,
            "symbol": "MES",
            "market": "Futures",
            "opportunity": {
                "score": 20,
                "confidence": 20,
                "grade": "D",
                "recommendation": "IGNORE",
                "reasons": ["Poor confluence"],
            },
        }

        result = self.engine.evaluate(context)

        self.assertEqual(result.signal, "WAIT")

if __name__ == "__main__":
    unittest.main()
