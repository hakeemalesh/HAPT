"""
HAPT Performance Metrics
------------------------

Calculates professional trading statistics from
a TradeJournal.
"""


class PerformanceMetrics:
    """Calculates trading performance metrics."""

    @staticmethod
    def calculate(trades):
        """Calculate performance metrics."""

        total = len(trades)

        winners = [
            t for t in trades
            if t["net_pnl"] > 0
        ]

        losers = [
            t for t in trades
            if t["net_pnl"] < 0
        ]

        breakeven = [
            t for t in trades
            if t["net_pnl"] == 0
        ]

        gross_profit = round(
            sum(t["net_pnl"] for t in winners),
            2,
        )

        gross_loss = round(
            abs(sum(t["net_pnl"] for t in losers)),
            2,
        )

        net_profit = round(
            gross_profit - gross_loss,
            2,
        )

        winning_trades = len(winners)
        losing_trades = len(losers)

        win_rate = (
            round(
                (winning_trades / total) * 100,
                2,
            )
            if total
            else 0.0
        )

        loss_rate = (
            round(
                (losing_trades / total) * 100,
                2,
            )
            if total
            else 0.0
        )

        average_winner = (
            round(
                gross_profit / winning_trades,
                2,
            )
            if winning_trades
            else 0.0
        )

        average_loser = (
            round(
                gross_loss / losing_trades,
                2,
            )
            if losing_trades
            else 0.0
        )

        largest_winner = (
            max(
                (t["net_pnl"] for t in winners),
                default=0.0,
            )
        )

        largest_loser = (
            min(
                (t["net_pnl"] for t in losers),
                default=0.0,
            )
        )

        profit_factor = (
            round(
                gross_profit / gross_loss,
                2,
            )
            if gross_loss > 0
            else 0.0
        )

        return {
            "total_trades": total,
            "winning_trades": winning_trades,
            "losing_trades": losing_trades,
            "breakeven_trades": len(breakeven),
            "gross_profit": gross_profit,
            "gross_loss": gross_loss,
            "net_profit": net_profit,
            "win_rate": win_rate,
            "loss_rate": loss_rate,
            "average_winner": average_winner,
            "average_loser": average_loser,
            "largest_winner": largest_winner,
            "largest_loser": largest_loser,
            "profit_factor": profit_factor,
        }
