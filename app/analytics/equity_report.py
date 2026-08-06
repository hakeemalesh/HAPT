"""
HAPT Professional Equity Report
-------------------------------

Formats portfolio analytics into a
professional multi-line report.
"""


class EquityReport:
    """Formats a portfolio equity report."""

    @staticmethod
    def build(
        *,
        starting_balance: float,
        ending_balance: float,
        portfolio_stats: dict,
        drawdown_stats: dict,
        streak_stats: dict,
        distribution_stats: dict,
    ) -> str:
        """
        Build a formatted equity report.

        Returns
        -------
        str
        """

        return f"""
==============================================
             HAPT EQUITY REPORT
==============================================

Portfolio
----------------------------------------------
Starting Balance : ${starting_balance:,.2f}
Ending Balance   : ${ending_balance:,.2f}

Net Profit       : ${portfolio_stats['net_profit']:,.2f}

Performance
----------------------------------------------
Total Trades     : {portfolio_stats['total_trades']}

Win Rate         : {portfolio_stats['win_rate']:.2f}%

Loss Rate        : {portfolio_stats['loss_rate']:.2f}%

Profit Factor    : {portfolio_stats['profit_factor']:.2f}

Expectancy       : ${portfolio_stats['expectancy']:,.2f}

Risk
----------------------------------------------
Maximum Drawdown : ${drawdown_stats['max_drawdown']:,.2f}

Current Drawdown : ${drawdown_stats['current_drawdown']:,.2f}

Trade Behaviour
----------------------------------------------
Longest Win      : {streak_stats['longest_win_streak']}

Longest Loss     : {streak_stats['longest_loss_streak']}

Largest Win      : ${distribution_stats['largest_win']:,.2f}

Largest Loss     : ${distribution_stats['largest_loss']:,.2f}

Average Win      : ${distribution_stats['average_win']:,.2f}

Average Loss     : ${distribution_stats['average_loss']:,.2f}

==============================================
""".strip()
