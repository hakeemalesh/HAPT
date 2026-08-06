"""
HAPT Optimization Result
------------------------

Represents the outcome of evaluating one
strategy configuration.
"""

from dataclasses import dataclass

from app.optimization.strategy_parameters import StrategyParameters


@dataclass(frozen=True, slots=True)
class OptimizationResult:
    """
    Result of evaluating one strategy.
    """

    parameters: StrategyParameters

    total_trades: int

    net_profit: float

    win_rate: float

    profit_factor: float

    expectancy: float

    max_drawdown: float
