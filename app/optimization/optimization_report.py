"""
HAPT Professional Optimization Report
-------------------------------------

Generates a professional summary of
optimization results.
"""

from app.optimization.monte_carlo import MonteCarloResult
from app.optimization.optimization_result import OptimizationResult


class OptimizationReport:
    """Builds professional optimization reports."""

    @staticmethod
    def generate(
        *,
        best_result: OptimizationResult,
        walk_forward_summary: dict,
        monte_carlo: MonteCarloResult,
        ranking: int = 1,
    ) -> dict:
        """
        Generate a professional optimization report.
        """

        return {
            "instrument": best_result.parameters.instrument,
            "timeframe": best_result.parameters.timeframe,
            "ranking": ranking,
            "total_trades": best_result.total_trades,
            "net_profit": best_result.net_profit,
            "profit_factor": best_result.profit_factor,
            "expectancy": best_result.expectancy,
            "win_rate": best_result.win_rate,
            "max_drawdown": best_result.max_drawdown,
            "walk_forward": walk_forward_summary,
            "monte_carlo": {
                "simulations": monte_carlo.simulations,
                "average_profit": monte_carlo.average_profit,
                "best_profit": monte_carlo.best_profit,
                "worst_profit": monte_carlo.worst_profit,
            },
            "summary": (
                f"Rank #{ranking} strategy for "
                f"{best_result.parameters.instrument} "
                f"({best_result.parameters.timeframe}) "
                f"generated net profit "
                f"{best_result.net_profit:.2f} "
                f"with profit factor "
                f"{best_result.profit_factor:.2f}."
            ),
        }
