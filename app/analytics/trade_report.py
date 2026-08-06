"""
HAPT Professional Trade Report
------------------------------

Generates a formatted performance report from
the calculated performance metrics.
"""


class TradeReport:
    """Formats performance metrics into a report."""

    @staticmethod
    def generate(metrics):
        """Generate a formatted report."""

        lines = [
            "=" * 58,
            "HAPT PROFESSIONAL PERFORMANCE REPORT",
            "=" * 58,
            "",
            "TRADING SUMMARY",
            "-" * 58,
            f"Total Trades      : {metrics['total_trades']}",
            f"Winning Trades    : {metrics['winning_trades']}",
            f"Losing Trades     : {metrics['losing_trades']}",
            f"Breakeven Trades  : {metrics['breakeven_trades']}",
            "",
            f"Win Rate          : {metrics['win_rate']:.2f}%",
            f"Loss Rate         : {metrics['loss_rate']:.2f}%",
            "",
            "FINANCIAL PERFORMANCE",
            "-" * 58,
            f"Gross Profit      : ${metrics['gross_profit']:.2f}",
            f"Gross Loss        : ${metrics['gross_loss']:.2f}",
            f"Net Profit        : ${metrics['net_profit']:.2f}",
            "",
            f"Profit Factor     : {metrics['profit_factor']:.2f}",
            "",
            "TRADE QUALITY",
            "-" * 58,
            f"Average Winner    : ${metrics['average_winner']:.2f}",
            f"Average Loser     : ${metrics['average_loser']:.2f}",
            f"Largest Winner    : ${metrics['largest_winner']:.2f}",
            f"Largest Loser     : ${metrics['largest_loser']:.2f}",
            "",
            "=" * 58,
        ]

        return "\n".join(lines)
