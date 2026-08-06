"""
HAPT Strategy Allocation Engine
-------------------------------

Validates and allocates strategies into
a portfolio.
"""

from dataclasses import dataclass

from app.portfolio.portfolio import (
    Portfolio,
    StrategyAllocation,
)


@dataclass(frozen=True, slots=True)
class AllocationResult:
    """
    Result of an allocation attempt.
    """

    success: bool
    message: str
    strategy_count: int
    remaining_capital: float
    remaining_risk: float


class StrategyAllocationEngine:
    """
    Handles portfolio allocations.
    """

    MAX_TOTAL_RISK = 100.0

    @staticmethod
    def allocate(
        portfolio: Portfolio,
        strategy: StrategyAllocation,
    ) -> AllocationResult:
        """
        Validate and allocate a strategy.
        """

        # Duplicate strategy name
        if any(
            s.strategy_name == strategy.strategy_name
            for s in portfolio.strategies
        ):
            return AllocationResult(
                False,
                "Duplicate strategy name.",
                portfolio.strategy_count,
                portfolio.available_capital,
                StrategyAllocationEngine.MAX_TOTAL_RISK
                - portfolio.total_risk,
            )

        # Capital validation
        if (
            strategy.capital_allocation
            > portfolio.available_capital
        ):
            return AllocationResult(
                False,
                "Insufficient available capital.",
                portfolio.strategy_count,
                portfolio.available_capital,
                StrategyAllocationEngine.MAX_TOTAL_RISK
                - portfolio.total_risk,
            )

        # Risk validation
        if (
            portfolio.total_risk
            + strategy.risk_allocation
            > StrategyAllocationEngine.MAX_TOTAL_RISK
        ):
            return AllocationResult(
                False,
                "Portfolio risk limit exceeded.",
                portfolio.strategy_count,
                portfolio.available_capital,
                StrategyAllocationEngine.MAX_TOTAL_RISK
                - portfolio.total_risk,
            )

        portfolio.add_strategy(strategy)

        return AllocationResult(
            True,
            "Strategy allocated.",
            portfolio.strategy_count,
            portfolio.available_capital,
            StrategyAllocationEngine.MAX_TOTAL_RISK
            - portfolio.total_risk,
        )
