"""
HAPT Opportunity Engine
-----------------------

Calculates an opportunity score from the current
market context.
"""

from app.rules.trading_rules import TradingRules


class OpportunityEngine:
    """Calculates the market opportunity score."""

    def score(self, context):
        """Calculate the opportunity score."""

        trend = self._trend(context)

        trend_score = (
            TradingRules.EMA_ALIGNMENT_SCORE
            if trend in ("Bullish", "Bearish")
            else 0
        )

        momentum_score = self._momentum_score(context)
        volume_score = self._volume_score(context)
        atr_score = self._atr_score(context)
        vwap_score = self._vwap_score(context)
        market_structure_score = self._market_structure_score(context)
        session_score = self._session_score(context)

        overall = (
            trend_score
            + momentum_score
            + volume_score
            + atr_score
            + vwap_score
            + market_structure_score
            + session_score
        )

        overall = min(overall, TradingRules.MAX_SCORE)

        return {
            "overall": overall,
            "trend": trend_score,
            "momentum": momentum_score,
            "volume": volume_score,
            "atr": atr_score,
            "vwap": vwap_score,
            "market_structure": market_structure_score,
            "session": session_score,
            "grade": self._grade(overall),
        }

    def _trend(self, context):
        """Determine EMA alignment."""

        ema9 = context.get("ema_9")
        ema20 = context.get("ema_20")
        ema50 = context.get("ema_50")
        ema200 = context.get("ema_200")

        if None in (ema9, ema20, ema50, ema200):
            return "Unknown"

        if ema9 > ema20 > ema50 > ema200:
            return "Bullish"

        if ema9 < ema20 < ema50 < ema200:
            return "Bearish"

        return "Sideways"

    def _momentum_score(self, context):
        """Calculate momentum score."""

        score = 0

        rsi = context.get("rsi")

        if rsi is not None:
            if (
                rsi >= TradingRules.RSI_BULLISH
                or rsi <= TradingRules.RSI_BEARISH
            ):
                score += TradingRules.RSI_SCORE

        if context.get("macd") is not None:
            score += TradingRules.MACD_SCORE

        return score

    def _volume_score(self, context):
        """Calculate relative volume score."""

        rv = context.get("relative_volume")

        if (
            rv is not None
            and rv >= TradingRules.RELATIVE_VOLUME_HIGH
        ):
            return TradingRules.RELATIVE_VOLUME_SCORE

        return 0

    def _atr_score(self, context):
        """Calculate ATR volatility score."""

        atr = context.get("atr")

        if atr is None:
            return TradingRules.ATR_POOR_SCORE

        if atr >= TradingRules.ATR_GOOD_THRESHOLD:
            return TradingRules.ATR_GOOD_SCORE

        if atr >= TradingRules.ATR_FAIR_THRESHOLD:
            return TradingRules.ATR_FAIR_SCORE

        return TradingRules.ATR_POOR_SCORE

    def _vwap_score(self, context):
        """Calculate VWAP position score."""

        price = context.get("price")
        vwap = context.get("vwap")

        if price is None or vwap is None:
            return TradingRules.VWAP_POOR_SCORE

        if price >= vwap:
            return TradingRules.VWAP_GOOD_SCORE

        return TradingRules.VWAP_POOR_SCORE

    def _market_structure_score(self, context):
        """Calculate market structure score."""

        structure = context.get("market_structure")

        if structure in ("Bullish", "Bearish"):
            return TradingRules.MARKET_STRUCTURE_GOOD_SCORE

        return TradingRules.MARKET_STRUCTURE_POOR_SCORE

    def _session_score(self, context):
        """Calculate session score."""

        return min(
            context.get("session_score", 0),
            TradingRules.SESSION_MAX_SCORE
        )

    def _grade(self, score):
        """Convert score into grade."""

        if score >= TradingRules.GRADE_A_PLUS:
            return "A+"

        if score >= TradingRules.GRADE_A:
            return "A"

        if score >= TradingRules.GRADE_B:
            return "B"

        if score >= TradingRules.GRADE_C:
            return "C"

        return "D"