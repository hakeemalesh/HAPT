"""
HAPT Decision Engine
--------------------

Evaluates market conditions and produces a trading
decision based on a weighted scoring model.
"""

from app.models.decision import Decision
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
        """

        #
        # ------------------------------------------
        # Market Session Guard
        # ------------------------------------------
        #

        if not context.get("market_open", False):

            decision = Decision()

            decision.symbol = context.get(
                "symbol",
                "",
            )

            decision.market = context.get(
                "market",
                "",
            )

            decision.score = 0

            decision.confidence = 0.0

            decision.grade = "D"

            decision.signal = "WAIT"

            decision.reasons = [
                "Market is closed."
            ]

            decision.details = {
                "session": context.get(
                    "session",
                    "Market Closed",
                )
            }

            return decision

        score = 0

        details = {}

        reasons = []

        # ------------------------------------------
        # EMA Alignment
        # ------------------------------------------

        trend = self._trend(context)

        if trend == "Bullish":
            score += TradingRules.EMA_ALIGNMENT_SCORE
            reasons.append("Bullish EMA alignment")

        elif trend == "Bearish":
            score += TradingRules.EMA_ALIGNMENT_SCORE
            reasons.append("Bearish EMA alignment")

        else:
            reasons.append("No clear EMA trend")

        details["trend"] = trend

        # ------------------------------------------
        # VWAP
        # ------------------------------------------

        price = context.get("price")
        vwap = context.get("vwap")

        if price is not None and vwap is not None:

            if price >= vwap:

                score += TradingRules.VWAP_GOOD_SCORE

                details["vwap"] = "Bullish"

                reasons.append(
                    "Price trading above VWAP"
                )

            else:

                score += TradingRules.VWAP_POOR_SCORE

                details["vwap"] = "Bearish"

                reasons.append(
                    "Price trading below VWAP"
                )

        else:

            details["vwap"] = "Unknown"

        # ------------------------------------------
        # RSI
        # ------------------------------------------

        rsi = context.get("rsi")

        if rsi is not None:

            if rsi >= TradingRules.RSI_BULLISH:
                score += TradingRules.RSI_SCORE
                details["rsi"] = "Bullish"
                reasons.append(
                    "RSI confirms bullish momentum"
                )

            elif rsi <= TradingRules.RSI_BEARISH:
                score += TradingRules.RSI_SCORE
                details["rsi"] = "Bearish"
                reasons.append(
                    "RSI confirms bearish momentum"
                )

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
            reasons.append("MACD available")
        else:
            details["macd"] = "Unavailable"

        # ------------------------------------------
        # ATR
        # ------------------------------------------

        atr = context.get("atr")

        if atr is not None:

            if atr >= TradingRules.ATR_GOOD_THRESHOLD:

                score += TradingRules.ATR_GOOD_SCORE

                details["atr"] = "Good"

                reasons.append(
                    "ATR confirms healthy volatility"
                )

            elif atr >= TradingRules.ATR_FAIR_THRESHOLD:

                score += TradingRules.ATR_FAIR_SCORE

                details["atr"] = "Fair"

                reasons.append(
                    "ATR indicates moderate volatility"
                )

            else:

                score += TradingRules.ATR_POOR_SCORE

                details["atr"] = "Low"

        else:

            details["atr"] = "Unknown"

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
            reasons.append(
                "High relative volume"
            )
        else:
            details["volume"] = "Normal"

        # ------------------------------------------
        # Session
        # ------------------------------------------

        session_score = context.get("session_score")

        if session_score is not None:

            score += min(
                session_score,
                TradingRules.SESSION_MAX_SCORE,
            )

        details["session"] = context.get(
            "session",
            "Unknown",
        )

        if context.get("session"):
            reasons.append(
                f"Trading during {context.get('session')}"
            )

        # ------------------------------------------
        # Grade
        # ------------------------------------------

        score = min(score, self.max_score)

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

        decision = Decision()

        decision.symbol = context.get(
            "symbol",
            "",
        )

        decision.market = context.get(
            "market",
            "",
        )

        decision.score = score

        decision.confidence = round(
            (score / self.max_score) * 100,
            1,
        )

        decision.grade = grade

        decision.signal = signal

        decision.reasons = reasons

        decision.details = details

        return decision

    def _trend(self, context):
        """
        Determine EMA trend.
        """

        ema9 = context.get("ema_9")
        ema20 = context.get("ema_20")
        ema50 = context.get("ema_50")
        ema200 = context.get("ema_200")

        if any(
            value is None
            for value in (
                ema9,
                ema20,
                ema50,
                ema200,
            )
        ):
            return "Unknown"

        if ema9 > ema20 > ema50 > ema200:
            return "Bullish"

        if ema9 < ema20 < ema50 < ema200:
            return "Bearish"

        return "Sideways"