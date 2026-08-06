"""
HAPT Portfolio Statistics Engine
--------------------------------

Calculates professional portfolio statistics
from completed trade results.
"""


class PortfolioStatistics:
    """Calculates portfolio performance statistics."""

    @staticmethod
    def calculate(
        trade_results: list[float],
    ) -> dict:
        """
        Calculate portfolio statistics.

        Parameters
        ----------
        trade_results : list[float]
            Net P&L of completed trades.

        Returns
        -------
        dict
        """

        total_trades = len(trade_results)

        winning = [x for x in trade_results if x > 0]
        losing = [x for x in trade_results if x < 0]
        breakeven = [x for x in trade_results if x == 0]

        gross_profit = sum(winning)
        gross_loss = abs(sum(losing))
        net_profit = gross_profit - gross_loss

        win_rate = (
            (len(winning) / total_trades) * 100
            if total_trades
            else 0.0
        )

        loss_rate = (
            (len(losing) / total_trades) * 100
            if total_trades
            else 0.0
        )

        profit_factor = (
            gross_profit / gross_loss
            if gross_loss > 0
            else 0.0
        )

        average_win = (
            gross_profit / len(winning)
            if winning
            else 0.0
        )

        average_loss = (
            gross_loss / len(losing)
            if losing
            else 0.0
        )

        expectancy = (
            net_profit / total_trades
            if total_trades
            else 0.0
        )

        return {
            "total_trades": total_trades,
            "winning_trades": len(winning),
            "losing_trades": len(losing),
            "breakeven_trades": len(breakeven),
            "win_rate": round(win_rate, 2),
            "loss_rate": round(loss_rate, 2),
            "gross_profit": round(gross_profit, 2),
            "gross_loss": round(gross_loss, 2),
            "net_profit": round(net_profit, 2),
            "average_win": round(average_win, 2),
            "average_loss": round(average_loss, 2),
            "largest_win": max(winning) if winning else 0.0,
            "largest_loss": min(losing) if losing else 0.0,
            "profit_factor": round(profit_factor, 2),
            "expectancy": round(expectancy, 2),
        }
