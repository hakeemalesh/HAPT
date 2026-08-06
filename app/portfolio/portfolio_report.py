"""
HAPT Professional Portfolio Report
----------------------------------

Generates a professional portfolio report
from portfolio analytics.
"""

from app.portfolio.correlation_analysis import CorrelationPair
from app.portfolio.portfolio import Portfolio
from app.portfolio.rebalancer import RebalanceRecommendation
from app.portfolio.risk_engine import PortfolioRiskSummary


class PortfolioReport:
    """
    Generates professional portfolio reports.
    """

    @staticmethod
    def generate(
        *,
        portfolio: Portfolio,
        risk_summary: PortfolioRiskSummary,
        correlations: list[CorrelationPair],
        recommendations: list[RebalanceRecommendation],
    ) -> dict:
        """
        Generate a professional portfolio report.
        """

        high_correlations = sum(
            1
            for pair in correlations
            if abs(pair.correlation) >= 0.80
        )

        if recommendations:
            recommendation_summary = (
                f"{len(recommendations)} rebalance "
                f"recommendation(s) generated."
            )
        else:
            recommendation_summary = (
                "Portfolio is already balanced."
            )

        summary = (
            f"Portfolio '{portfolio.name}' contains "
            f"{portfolio.strategy_count} strategies with "
            f"{portfolio.capital_utilization if hasattr(portfolio, 'capital_utilization') else risk_summary.capital_utilization:.2f}% "
            f"capital utilization and "
            f"{risk_summary.risk_utilization:.2f}% "
            f"risk utilization."
        )

        return {
            "portfolio_name": portfolio.name,
            "strategy_count": portfolio.strategy_count,
            "allocated_capital": portfolio.allocated_capital,
            "available_capital": portfolio.available_capital,
            "total_risk": risk_summary.total_risk,
            "remaining_risk": risk_summary.remaining_risk,
            "capital_utilization": (
                risk_summary.capital_utilization
            ),
            "risk_utilization": (
                risk_summary.risk_utilization
            ),
            "within_limits": risk_summary.within_limits,
            "correlation_pairs": len(correlations),
            "high_correlations": high_correlations,
            "rebalance_recommendations": len(
                recommendations
            ),
            "recommendation_summary": (
                recommendation_summary
            ),
            "summary": summary,
            "generated_at": portfolio.created_at,
        }
