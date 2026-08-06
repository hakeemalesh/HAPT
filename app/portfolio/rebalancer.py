"""
HAPT Portfolio Rebalancer
-------------------------

Generates portfolio rebalance
recommendations.
"""

from dataclasses import dataclass

from app.portfolio.portfolio import Portfolio


@dataclass(frozen=True, slots=True)
class RebalanceRecommendation:
    """
    Portfolio rebalance recommendation.
    """

    strategy_name: str
    current_capital: float
    target_capital: float
    adjustment: float
    action: str


class PortfolioRebalancer:
    """
    Generates rebalance recommendations.
    """

    @staticmethod
    def rebalance(
        portfolio: Portfolio,
        target_allocations: dict[str, float],
    ) -> list[RebalanceRecommendation]:
        """
        Compare current and target allocations.
        """

        recommendations: list[
            RebalanceRecommendation
        ] = []

        for strategy in portfolio.strategies:

            target = target_allocations.get(
                strategy.strategy_name,
                strategy.capital_allocation,
            )

            adjustment = round(
                target - strategy.capital_allocation,
                2,
            )

            if adjustment > 0:
                action = "INCREASE"
            elif adjustment < 0:
                action = "REDUCE"
            else:
                action = "NONE"

            recommendations.append(
                RebalanceRecommendation(
                    strategy_name=strategy.strategy_name,
                    current_capital=strategy.capital_allocation,
                    target_capital=target,
                    adjustment=adjustment,
                    action=action,
                )
            )

        return recommendations
