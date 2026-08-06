"""
HAPT Portfolio Model
--------------------

Core portfolio models for managing multiple
trading strategies.
"""

from dataclasses import dataclass, field
from datetime import UTC, datetime


@dataclass(frozen=True, slots=True)
class StrategyAllocation:
    """
    Represents a strategy within a portfolio.
    """

    strategy_name: str
    instrument: str
    timeframe: str

    capital_allocation: float
    risk_allocation: float

    status: str = "ACTIVE"


@dataclass(slots=True)
class Portfolio:
    """
    Represents a portfolio of trading strategies.
    """

    name: str

    initial_capital: float

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    strategies: list[StrategyAllocation] = field(
        default_factory=list
    )

    def add_strategy(
        self,
        strategy: StrategyAllocation,
    ) -> None:
        """
        Add a strategy to the portfolio.
        """

        self.strategies.append(strategy)

    @property
    def strategy_count(self) -> int:
        """
        Number of strategies.
        """

        return len(self.strategies)

    @property
    def allocated_capital(self) -> float:
        """
        Total allocated capital.
        """

        return round(
            sum(
                strategy.capital_allocation
                for strategy in self.strategies
            ),
            2,
        )

    @property
    def available_capital(self) -> float:
        """
        Remaining unallocated capital.
        """

        return round(
            self.initial_capital
            - self.allocated_capital,
            2,
        )

    @property
    def total_risk(self) -> float:
        """
        Total allocated portfolio risk.
        """

        return round(
            sum(
                strategy.risk_allocation
                for strategy in self.strategies
            ),
            2,
        )
