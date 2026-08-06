"""
HAPT Strategy Benchmark Engine
------------------------------

Benchmarks research projects using their
best optimization results.
"""

from dataclasses import dataclass

from app.optimization.optimization_result import OptimizationResult


@dataclass(frozen=True, slots=True)
class BenchmarkEntry:
    """
    One benchmark entry.
    """

    project_name: str
    result: OptimizationResult


class StrategyBenchmarkEngine:
    """
    Benchmarks research projects.
    """

    VALID_METRICS = {
        "net_profit",
        "profit_factor",
        "expectancy",
        "win_rate",
        "max_drawdown",
    }

    @staticmethod
    def rank(
        entries: list[BenchmarkEntry],
        metric: str = "net_profit",
    ) -> list[BenchmarkEntry]:
        """
        Rank benchmark entries.
        """

        if metric not in StrategyBenchmarkEngine.VALID_METRICS:
            raise ValueError(
                f"Unsupported benchmark metric: {metric}"
            )

        reverse = metric != "max_drawdown"

        return sorted(
            entries,
            key=lambda entry: getattr(entry.result, metric),
            reverse=reverse,
        )

    @staticmethod
    def winner(
        entries: list[BenchmarkEntry],
        metric: str = "net_profit",
    ) -> BenchmarkEntry | None:
        """
        Return the highest-ranked entry.
        """

        ranked = StrategyBenchmarkEngine.rank(
            entries,
            metric=metric,
        )

        if not ranked:
            return None

        return ranked[0]
