"""
HAPT Optimization Engine
------------------------

Coordinates optimization runs and produces
OptimizationResult objects.
"""

from app.optimization.optimization_result import OptimizationResult
from app.optimization.strategy_parameters import StrategyParameters


class OptimizationEngine:
    """Evaluates strategy configurations."""

    @staticmethod
    def evaluate(
        *,
        parameters: StrategyParameters,
        total_trades: int,
        net_profit: float,
        win_rate: float,
        profit_factor: float,
        expectancy: float,
        max_drawdown: float,
    ) -> OptimizationResult:
        """
        Build one optimization result.

        In later nodes this method will call the
        replay engine automatically. For now it
        creates a strongly typed result object.
        """

        return OptimizationResult(
            parameters=parameters,
            total_trades=total_trades,
            net_profit=net_profit,
            win_rate=win_rate,
            profit_factor=profit_factor,
            expectancy=expectancy,
            max_drawdown=max_drawdown,
        )