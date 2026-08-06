"""
HAPT Portfolio Analytics Dashboard
----------------------------------

Aggregates all portfolio analytics into
a single dashboard object.
"""


class PortfolioDashboard:
    """Builds the complete portfolio dashboard."""

    @staticmethod
    def build(
        *,
        equity_curve: list[float],
        portfolio_stats: dict,
        drawdown_stats: dict,
        streak_stats: dict,
        distribution_stats: dict,
        report: str,
    ) -> dict:
        """
        Build the complete analytics dashboard.

        Returns
        -------
        dict
        """

        return {
            "equity_curve": equity_curve,
            "portfolio": portfolio_stats,
            "drawdown": drawdown_stats,
            "streaks": streak_stats,
            "distribution": distribution_stats,
            "report": report,
        }
