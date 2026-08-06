"""
HAPT Research Project
---------------------

Defines a quantitative research project that
groups together multiple optimization experiments.
"""

from dataclasses import dataclass, field
from datetime import UTC, datetime


@dataclass(frozen=True, slots=True)
class ResearchProject:
    """
    Represents a research project.
    """

    name: str

    objective: str

    instrument: str

    timeframe: str

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    status: str = "CREATED"

    total_experiments: int = 0

    completed_experiments: int = 0

    notes: str = ""

    @property
    def progress(self) -> float:
        """
        Percentage of completed experiments.
        """

        if self.total_experiments == 0:
            return 0.0

        return round(
            self.completed_experiments
            / self.total_experiments
            * 100.0,
            2,
        )

    @property
    def is_complete(self) -> bool:
        """
        Whether every experiment has completed.
        """

        return (
            self.total_experiments > 0
            and self.completed_experiments
            >= self.total_experiments
        )
