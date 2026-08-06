"""
HAPT Trade Distribution Analysis
--------------------------------

Analyzes the statistical distribution of
completed trade results.
"""

from statistics import median


class TradeDistribution:
    """Calculates trade distribution statistics."""

    @staticmethod
    def calculate(
        trade_results: list[float],
    ) -> dict:
        """
        Analyze completed trades.

        Parameters
        ----------
        trade_results : list[float]

        Returns
        -------
        dict
        """

        winners = sorted(
            [x for x in trade_results if x > 0]
        )

        losers = sorted(
            [x for x in trade_results if x < 0]
        )

        average_win = (
            sum(winners) / len(winners)
            if winners
            else 0.0
        )

        average_loss = (
            abs(sum(losers)) / len(losers)
            if losers
            else 0.0
        )

        median_win = (
            median(winners)
            if winners
            else 0.0
        )

        median_loss = (
            median(losers)
            if losers
            else 0.0
        )

        win_loss_ratio = (
            average_win / average_loss
            if average_loss > 0
            else 0.0
        )

        return {
            "largest_win": max(winners) if winners else 0.0,
            "largest_loss": min(losers) if losers else 0.0,
            "average_win": round(average_win, 2),
            "average_loss": round(average_loss, 2),
            "median_win": round(median_win, 2),
            "median_loss": round(median_loss, 2),
            "win_loss_ratio": round(win_loss_ratio, 2),
            "winning_trades": len(winners),
            "losing_trades": len(losers),
        }
