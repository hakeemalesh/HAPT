"""
HAPT Strategy Ranking Engine
----------------------------

Ranks optimization results according to
selected performance metrics.
"""

from app.optimization.optimization_result import OptimizationResult


class StrategyRanking:
    """Ranks optimization results."""

    VALID_METRICS = {
        "net_profit",
        "profit_factor",
        "expectancy",
        "win_rate",
        "max_drawdown",
    }

    @staticmethod
    def rank(
        results: list[OptimizationResult],
        metric: str = "net_profit",
    ) -> list[OptimizationResult]:
        """
        Rank optimization results.

        Parameters
        ----------
        results
            Optimization results.

        metric
            Ranking metric.

        Returns
        -------
        list[OptimizationResult]
        """

        if metric not in StrategyRanking.VALID_METRICS:
            raise ValueError(
                f"Unsupported ranking metric: {metric}"
            )

        reverse = metric != "max_drawdown"

        return sorted(
            results,
            key=lambda r: getattr(r, metric),
            reverse=reverse,
        )
