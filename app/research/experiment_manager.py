"""
HAPT Experiment Manager
-----------------------

Manages optimization experiments within a
research project.
"""

from dataclasses import dataclass, field
from datetime import UTC, datetime

from app.optimization.strategy_parameters import StrategyParameters


@dataclass(frozen=True, slots=True)
class ResearchExperiment:
    """
    Represents a single optimization experiment.
    """

    experiment_id: int

    parameters: StrategyParameters

    status: str = "QUEUED"

    score: float = 0.0

    started_at: datetime | None = None

    completed_at: datetime | None = None

    notes: str = ""


@dataclass(slots=True)
class ExperimentManager:
    """
    Manages research experiments.
    """

    experiments: list[ResearchExperiment] = field(
        default_factory=list
    )

    def add(
        self,
        parameters: StrategyParameters,
    ) -> ResearchExperiment:
        """
        Add a new experiment.
        """

        experiment = ResearchExperiment(
            experiment_id=len(self.experiments) + 1,
            parameters=parameters,
        )

        self.experiments.append(experiment)

        return experiment

    def start(
        self,
        experiment_id: int,
    ) -> None:
        """
        Mark an experiment as running.
        """

        experiment = self.experiments[experiment_id - 1]

        self.experiments[experiment_id - 1] = ResearchExperiment(
            experiment_id=experiment.experiment_id,
            parameters=experiment.parameters,
            status="RUNNING",
            score=experiment.score,
            started_at=datetime.now(UTC),
            completed_at=experiment.completed_at,
            notes=experiment.notes,
        )

    def complete(
        self,
        experiment_id: int,
        score: float,
    ) -> None:
        """
        Mark an experiment as completed.
        """

        experiment = self.experiments[experiment_id - 1]

        self.experiments[experiment_id - 1] = ResearchExperiment(
            experiment_id=experiment.experiment_id,
            parameters=experiment.parameters,
            status="COMPLETED",
            score=score,
            started_at=experiment.started_at,
            completed_at=datetime.now(UTC),
            notes=experiment.notes,
        )

    @property
    def queued(self) -> int:
        return sum(
            e.status == "QUEUED"
            for e in self.experiments
        )

    @property
    def running(self) -> int:
        return sum(
            e.status == "RUNNING"
            for e in self.experiments
        )

    @property
    def completed(self) -> int:
        return sum(
            e.status == "COMPLETED"
            for e in self.experiments
        )
