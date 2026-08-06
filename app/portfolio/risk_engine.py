"""
HAPT Portfolio Risk Engine
--------------------------

Portfolio-wide risk analysis.
"""

from dataclasses import dataclass

from app.portfolio.portfolio import Portfolio


@dataclass(frozen=True, slots=True)
class PortfolioRiskSummary:
    """
    Portfolio risk summary.
    """

    total_risk: float
    remaining_risk: float
    capital_utilization: float
    risk_utilization: float
    within_limits: bool


class PortfolioRiskEngine:
    """
    Portfolio risk calculations.
    """

    MAX_PORTFOLIO_RISK = 100.0

    @staticmethod
    def summarize(
        portfolio: Portfolio,
    ) -> PortfolioRiskSummary:
        """
        Produce a portfolio risk summary.
        """

        total_risk = round(
            portfolio.total_risk,
            2,
        )

        remaining_risk = round(
            PortfolioRiskEngine.MAX_PORTFOLIO_RISK
            - total_risk,
            2,
        )

        capital_utilization = round(
            (
                portfolio.allocated_capital
                / portfolio.initial_capital
            )
            * 100,
            2,
        ) if portfolio.initial_capital > 0 else 0.0

        risk_utilization = round(
            (
                total_risk
                / PortfolioRiskEngine.MAX_PORTFOLIO_RISK
            )
            * 100,
            2,
        )

        return PortfolioRiskSummary(
            total_risk=total_risk,
            remaining_risk=remaining_risk,
            capital_utilization=capital_utilization,
            risk_utilization=risk_utilization,
            within_limits=(
                total_risk
                <= PortfolioRiskEngine.MAX_PORTFOLIO_RISK
            ),
        )
