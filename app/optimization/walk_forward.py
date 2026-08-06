"""
HAPT Walk-Forward Validation
----------------------------

Provides the framework for walk-forward
validation over multiple optimization windows.
"""

from dataclasses import dataclass

from app.optimization.optimization_result import OptimizationResult


@dataclass(frozen=True, slots=True)
class WalkForwardWindow:
    """
    Represents one walk-forward validation window.
    """

    training_start: int
    training_end: int

    testing_start: int
    testing_end: int


class WalkForwardValidator:
    """Collects walk-forward validation results."""

    @staticmethod
    def validate(
        windows: list[WalkForwardWindow],
        results: list[OptimizationResult],
    ) -> dict:
        """
        Build a walk-forward validation summary.

        Parameters
        ----------
        windows
            Validation windows.

        results
            Optimization results obtained from
            the testing windows.

        Returns
        -------
        dict
        """

        completed = min(len(windows), len(results))

        average_profit = (
            sum(r.net_profit for r in results) / len(results)
            if results
            else 0.0
        )

        average_win_rate = (
            sum(r.win_rate for r in results) / len(results)
            if results
            else 0.0
        )

        return {
            "windows": completed,
            "average_net_profit": round(average_profit, 2),
            "average_win_rate": round(average_win_rate, 2),
            "completed": completed == len(windows),
        }
