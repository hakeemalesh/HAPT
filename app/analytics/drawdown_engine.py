"""
HAPT Drawdown Engine
--------------------

Calculates current and maximum drawdown
from an equity curve.
"""


class DrawdownEngine:
    """Calculates drawdown statistics."""

    @staticmethod
    def calculate(
        equity_curve: list[float],
    ) -> dict:
        """
        Calculate drawdown metrics.

        Returns
        -------
        dict
        """

        if not equity_curve:
            return {
                "peak": 0.0,
                "current_drawdown": 0.0,
                "max_drawdown": 0.0,
                "max_drawdown_pct": 0.0,
            }

        peak = equity_curve[0]
        max_drawdown = 0.0

        for equity in equity_curve:

            peak = max(peak, equity)

            drawdown = peak - equity

            max_drawdown = max(max_drawdown, drawdown)

        current_peak = max(equity_curve)
        current_drawdown = current_peak - equity_curve[-1]

        max_drawdown_pct = (
            (max_drawdown / current_peak) * 100
            if current_peak > 0
            else 0.0
        )

        return {
            "peak": round(current_peak, 2),
            "current_drawdown": round(
                current_drawdown,
                2,
            ),
            "max_drawdown": round(
                max_drawdown,
                2,
            ),
            "max_drawdown_pct": round(
                max_drawdown_pct,
                2,
            ),
        }
