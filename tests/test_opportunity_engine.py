"""HAPT Opportunity Engine Tests
-----------------------------

Unit tests for Opportunity Engine scoring.
"""

import unittest

from app.opportunity.opportunity_engine import OpportunityEngine
from app.rules.trading_rules import TradingRules


class TestOpportunityEngine(unittest.TestCase):
    def setUp(self):
        self.engine=OpportunityEngine()
    def test_returns_dictionary(self): self.assertIsInstance(self.engine.score({}),dict)
    def test_contains_required_keys(self):
        r=self.engine.score({})
        [self.assertIn(k,r) for k in ("overall","trend","momentum","volume","atr","vwap","market_structure","session","grade")]
    def test_grade_is_string(self): self.assertIsInstance(self.engine.score({})["grade"],str)
    def test_overall_is_integer(self): self.assertIsInstance(self.engine.score({})["overall"],int)
    def test_empty_context(self): self.assertIsNotNone(self.engine.score({}))
    def test_missing_values(self): self.assertIsInstance(self.engine.score({"ema_9":None,"ema_20":None,"ema_50":None,"ema_200":None}),dict)
    def test_bullish_trend_score(self): self.assertEqual(self.engine.score({"ema_9":105,"ema_20":104,"ema_50":103,"ema_200":100})["trend"],TradingRules.EMA_ALIGNMENT_SCORE)
    def test_bearish_trend_score(self): self.assertEqual(self.engine.score({"ema_9":100,"ema_20":101,"ema_50":102,"ema_200":103})["trend"],TradingRules.EMA_ALIGNMENT_SCORE)
    def test_sideways_trend_score(self): self.assertEqual(self.engine.score({"ema_9":102,"ema_20":101,"ema_50":103,"ema_200":100})["trend"],0)
    def test_high_relative_volume(self): self.assertEqual(self.engine.score({"relative_volume":TradingRules.RELATIVE_VOLUME_HIGH})["volume"],TradingRules.RELATIVE_VOLUME_SCORE)
    def test_bullish_rsi(self): self.assertEqual(self.engine.score({"rsi":TradingRules.RSI_BULLISH})["momentum"],TradingRules.RSI_SCORE)
    def test_macd_score(self): self.assertEqual(self.engine.score({"macd":0.75})["momentum"],TradingRules.MACD_SCORE)
    def test_poor_atr_score(self): self.assertEqual(self.engine.score({})["atr"],TradingRules.ATR_POOR_SCORE)
    def test_fair_atr_score(self): self.assertEqual(self.engine.score({"atr":TradingRules.ATR_FAIR_THRESHOLD})["atr"],TradingRules.ATR_FAIR_SCORE)
    def test_good_atr_score(self): self.assertEqual(self.engine.score({"atr":TradingRules.ATR_GOOD_THRESHOLD})["atr"],TradingRules.ATR_GOOD_SCORE)
    def test_missing_vwap_score(self): self.assertEqual(self.engine.score({})["vwap"],TradingRules.VWAP_POOR_SCORE)
    def test_price_above_vwap(self): self.assertEqual(self.engine.score({"price":101.0,"vwap":100.0})["vwap"],TradingRules.VWAP_GOOD_SCORE)
    def test_price_equal_vwap(self): self.assertEqual(self.engine.score({"price":100.0,"vwap":100.0})["vwap"],TradingRules.VWAP_GOOD_SCORE)
    def test_price_below_vwap(self): self.assertEqual(self.engine.score({"price":99.0,"vwap":100.0})["vwap"],TradingRules.VWAP_POOR_SCORE)
    def test_missing_market_structure(self): self.assertEqual(self.engine.score({})["market_structure"],TradingRules.MARKET_STRUCTURE_POOR_SCORE)
    def test_bullish_market_structure(self): self.assertEqual(self.engine.score({"market_structure":"Bullish"})["market_structure"],TradingRules.MARKET_STRUCTURE_GOOD_SCORE)
    def test_bearish_market_structure(self): self.assertEqual(self.engine.score({"market_structure":"Bearish"})["market_structure"],TradingRules.MARKET_STRUCTURE_GOOD_SCORE)
    def test_sideways_market_structure(self): self.assertEqual(self.engine.score({"market_structure":"Sideways"})["market_structure"],TradingRules.MARKET_STRUCTURE_POOR_SCORE)
    def test_complete_high_quality_setup(self):
        c={"ema_9":105,"ema_20":104,"ema_50":103,"ema_200":100,"rsi":TradingRules.RSI_BULLISH,"macd":0.8,"relative_volume":TradingRules.RELATIVE_VOLUME_HIGH,"atr":TradingRules.ATR_GOOD_THRESHOLD,"price":101.0,"vwap":100.0,"market_structure":"Bullish","session_score":TradingRules.SESSION_MAX_SCORE}
        r=self.engine.score(c)
        e=min(TradingRules.EMA_ALIGNMENT_SCORE+TradingRules.RSI_SCORE+TradingRules.MACD_SCORE+TradingRules.RELATIVE_VOLUME_SCORE+TradingRules.ATR_GOOD_SCORE+TradingRules.VWAP_GOOD_SCORE+TradingRules.MARKET_STRUCTURE_GOOD_SCORE+TradingRules.SESSION_MAX_SCORE,TradingRules.MAX_SCORE)
        self.assertEqual(r["overall"],e); self.assertIn(r["grade"],{"A+","A","B","C","D"})

if __name__=="__main__":
    unittest.main()
