"""
HAPT Research Dashboard
-----------------------

Builds a unified dashboard for research projects.
"""

from dataclasses import dataclass
from datetime import UTC, datetime

from app.research.benchmark_engine import (
    BenchmarkEntry,
    StrategyBenchmarkEngine,
)
from app.research.experiment_manager import ExperimentManager
from app.research.repository import ResearchRepository
from app.research.research_project import ResearchProject


@dataclass(frozen=True, slots=True)
class ResearchDashboard:
    """
    Builds a research dashboard.
    """

    @staticmethod
    def build(
        *,
        project: ResearchProject,
        experiments: ExperimentManager,
        repository: ResearchRepository,
        benchmark_entries: list[BenchmarkEntry],
        benchmark_metric: str = "net_profit",
    ) -> dict:
        """
        Build a research dashboard.
        """

        winner = StrategyBenchmarkEngine.winner(
            benchmark_entries,
            metric=benchmark_metric,
        )

        return {
            "project_name": project.name,
            "status": project.status,
            "progress": project.progress,
            "total_experiments": project.total_experiments,
            "completed_experiments": project.completed_experiments,
            "queued": experiments.queued,
            "running": experiments.running,
            "completed": experiments.completed,
            "repository_projects": repository.count,
            "benchmark_metric": benchmark_metric,
            "best_project": (
                winner.project_name
                if winner is not None
                else None
            ),
            "best_result": (
                winner.result.net_profit
                if winner is not None
                else None
            ),
            "generated_at": datetime.now(UTC),
        }
