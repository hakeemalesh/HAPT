"""
HAPT Decision Engine
--------------------

Evaluates market conditions and produces a trading
decision based on a weighted scoring model.
"""


class DecisionEngine:
    """Evaluates trading quality."""

    def __init__(self):
        """Initialize scoring rules."""

        self.max_score = 100

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
            score += 20

        elif trend == "Bearish":
            score += 20

        details["trend"] = trend

        # ------------------------------------------
        # VWAP
        # ------------------------------------------

        if context.get("vwap") is not None:
            score += 20
            details["vwap"] = "Available"
        else:
            details["vwap"] = "Unavailable"

        # ------------------------------------------
        # RSI
        # ------------------------------------------

        rsi = context.get("rsi")

        if rsi is not None:

            if rsi >= 60:
                score += 15
                details["rsi"] = "Bullish"

            elif rsi <= 40:
                score += 15
                details["rsi"] = "Bearish"

            else:
                details["rsi"] = "Neutral"

        else:
            details["rsi"] = "Unknown"

        # ------------------------------------------
        # MACD
        # ------------------------------------------

        if context.get("macd") is not None:
            score += 15
            details["macd"] = "Available"
        else:
            details["macd"] = "Unavailable"

        # ------------------------------------------
        # Relative Volume
        # ------------------------------------------

        rv = context.get("relative_volume")

        if rv is not None and rv >= 1.2:
            score += 15
            details["volume"] = "High"
        else:
            details["volume"] = "Normal"

        # ------------------------------------------
        # Session
        # ------------------------------------------

        session_score = context.get("session_score")

        if session_score is not None:
            score += min(session_score, 15)

        details["session"] = context.get("session")

        # ------------------------------------------
        # Final Decision
        # ------------------------------------------

        if score >= 90:
            signal = "BUY"

        elif score >= 75:
            signal = "BUY"

        elif score >= 60:
            signal = "WATCH"

        else:
            signal = "WAIT"

        return {

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