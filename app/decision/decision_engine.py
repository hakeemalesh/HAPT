"""
HAPT Decision Engine
--------------------

Evaluates market conditions and produces a trading
decision based on a weighted scoring model.
"""

from app.rules.trading_rules import TradingRules


class DecisionEngine:
    """Evaluates trading quality."""

    def __init__(self):
        """Initialize scoring rules."""

        self.max_score = TradingRules.MAX_SCORE

    def _grade(self, score):
        """
        Convert a score into a HAPT grade.
        """

        if score >= TradingRules.GRADE_A_PLUS:
            return "A+"

        if score >= TradingRules.GRADE_A:
            return "A"

        if score >= TradingRules.GRADE_B:
            return "B"

        if score >= TradingRules.GRADE_C:
            return "C"

        return "D"

    def evaluate(self, context):
        """
        Evaluate market context.

        Parameters
        ----------
        context : dict

        Returns
        -------
        dict
        """

        score = 0

        details = {}

        # ------------------------------------------
        # EMA Alignment
        # ------------------------------------------

        trend = self._trend(context)

        if trend == "Bullish":
            score += TradingRules.EMA_ALIGNMENT_SCORE

        elif trend == "Bearish":
            score += TradingRules.EMA_ALIGNMENT_SCORE

        details["trend"] = trend

        # ------------------------------------------
        # VWAP
        # ------------------------------------------

        if context.get("vwap") is not None:
            score += TradingRules.VWAP_SCORE
            details["vwap"] = "Available"
        else:
            details["vwap"] = "Unavailable"

        # ------------------------------------------
        # RSI
        # ------------------------------------------

        rsi = context.get("rsi")

        if rsi is not None:

            if rsi >= TradingRules.RSI_BULLISH:
                score += TradingRules.RSI_SCORE
                details["rsi"] = "Bullish"

            elif rsi <= TradingRules.RSI_BEARISH:
                score += TradingRules.RSI_SCORE
                details["rsi"] = "Bearish"

            else:
                details["rsi"] = "Neutral"

        else:
            details["rsi"] = "Unknown"

        # ------------------------------------------
        # MACD
        # ------------------------------------------

        if context.get("macd") is not None:
            score += TradingRules.MACD_SCORE
            details["macd"] = "Available"
        else:
            details["macd"] = "Unavailable"

        # ------------------------------------------
        # Relative Volume
        # ------------------------------------------

        rv = context.get("relative_volume")

        if (
            rv is not None
            and rv >= TradingRules.RELATIVE_VOLUME_HIGH
        ):
            score += TradingRules.RELATIVE_VOLUME_SCORE
            details["volume"] = "High"
        else:
            details["volume"] = "Normal"

        # ------------------------------------------
        # Session
        # ------------------------------------------

        session_score = context.get("session_score")

        if session_score is not None:
            score += min(
                session_score,
                TradingRules.SESSION_MAX_SCORE
            )

        details["session"] = context.get("session")

        # ------------------------------------------
        # Grade
        # ------------------------------------------

        grade = self._grade(score)

        # ------------------------------------------
        # Final Decision
        # ------------------------------------------

        if grade in ("A+", "A"):
            signal = "BUY"

        elif grade in ("B", "C"):
            signal = "WATCH"

        else:
            signal = "WAIT"

        return {

            "score": min(score, self.max_score),

            "grade": grade,

            "signal": signal,

            "confidence": min(score, self.max_score),

            "details": details
        }

    def _trend(self, context):
        """
        Determine EMA trend.
        """

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