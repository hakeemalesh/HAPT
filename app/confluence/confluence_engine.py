"""
HAPT Confluence Engine
----------------------

Combines signals from multiple analyzers into a
single professional opportunity assessment.
"""


class ConfluenceEngine:
    """
    Combines analyzer outputs into one
    confluence score.
    """

    @staticmethod
    def evaluate(
        ema_score,
        momentum_score,
        volume_score,
        atr_score,
        vwap_score,
        structure,
        session_score,
    ):
        """
        Evaluate overall market confluence.

        Returns
        -------
        dict
        """

        scores = {

            "ema": ema_score,

            "momentum": momentum_score,

            "volume": volume_score,

            "atr": atr_score,

            "vwap": vwap_score,

            "structure": (
                20
                if structure == "Bullish"
                else 20
                if structure == "Bearish"
                else 0
            ),

            "session": session_score,
        }

        total = sum(scores.values())

        confidence = min(total, 100)

        agreement = sum(
            1
            for value in scores.values()
            if value > 0
        )

        conflicts = len(scores) - agreement

        if confidence >= 90:

            grade = "A+"

            recommendation = "BUY"

        elif confidence >= 80:

            grade = "A"

            recommendation = "BUY"

        elif confidence >= 65:

            grade = "B"

            recommendation = "WATCH"

        elif confidence >= 50:

            grade = "C"

            recommendation = "WAIT"

        else:

            grade = "D"

            recommendation = "IGNORE"

        reasons = []

        if ema_score > 0:
            reasons.append("EMA alignment")

        if momentum_score > 0:
            reasons.append("Momentum confirmed")

        if volume_score > 0:
            reasons.append("Strong volume")

        if atr_score > 0:
            reasons.append("Healthy volatility")

        if vwap_score > 0:
            reasons.append("Price near favorable VWAP")

        if structure in ("Bullish", "Bearish"):
            reasons.append(
                f"{structure} market structure"
            )

        if session_score > 0:
            reasons.append("Favorable market session")

        return {

            "score": confidence,

            "confidence": confidence,

            "grade": grade,

            "recommendation": recommendation,

            "agreement": agreement,

            "conflicts": conflicts,

            "reasons": reasons,

            "scores": scores,
        }
