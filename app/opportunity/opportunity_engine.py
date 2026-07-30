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
        """
        Calculate the opportunity score.
        """

        trend_score = 0
        momentum_score = 0
        volume_score = 0
        atr_score = 0
        session_score = 0

        # -----------------------------
        # Trend
        # -----------------------------

        trend = self._trend(context)

        if trend in ("Bullish", "Bearish"):
            trend_score = TradingRules.EMA_ALIGNMENT_SCORE

        # -----------------------------
        # Momentum
        # -----------------------------

        rsi = context.get("rsi")

        if rsi is not None:
            if (
                rsi >= TradingRules.RSI_BULLISH
                or rsi <= TradingRules.RSI_BEARISH
            ):
                momentum_score += TradingRules.RSI_SCORE

        if context.get("macd") is not None:
            momentum_score += TradingRules.MACD_SCORE

        # -----------------------------
        # Volume
        # -----------------------------

        rv = context.get("relative_volume")

        if (
            rv is not None
            and rv >= TradingRules.RELATIVE_VOLUME_HIGH
        ):
            volume_score = TradingRules.RELATIVE_VOLUME_SCORE

        # -----------------------------
        # ATR
        # -----------------------------

        atr_score = self._atr_score(context)

        # -----------------------------
        # Session
        # -----------------------------

        session_score = min(
            context.get("session_score", 0),
            TradingRules.SESSION_MAX_SCORE
        )

        # -----------------------------
        # Overall
        # -----------------------------

        overall = (
            trend_score
            + momentum_score
            + volume_score
            + atr_score
            + session_score
        )

        overall = min(
            overall,
            TradingRules.MAX_SCORE
        )

        return {
            "overall": overall,
            "trend": trend_score,
            "momentum": momentum_score,
            "volume": volume_score,
            "atr": atr_score,
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