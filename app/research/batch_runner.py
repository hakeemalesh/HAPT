"""
HAPT Batch Optimization Runner
------------------------------

Executes batches of research experiments.
"""

from dataclasses import dataclass

from app.research.experiment_manager import ExperimentManager


@dataclass(frozen=True, slots=True)
class BatchRunSummary:
    """
    Summary of one batch execution.
    """

    total: int

    completed: int

    failed: int

    success_rate: float


class BatchOptimizationRunner:
    """
    Executes queued experiments sequentially.
    """

    @staticmethod
    def run(
        manager: ExperimentManager,
        score_provider=None,
    ) -> BatchRunSummary:
        """
        Execute every queued experiment.

        Parameters
        ----------
        manager
            Experiment manager.

        score_provider
            Optional callback:
                score_provider(experiment) -> float

            If omitted every experiment receives
            a score of 100.0.
        """

        completed = 0
        failed = 0

        for experiment in list(manager.experiments):

            if experiment.status != "QUEUED":
                continue

            try:

                manager.start(experiment.experiment_id)

                if score_provider is None:
                    score = 100.0
                else:
                    score = score_provider(experiment)

                manager.complete(
                    experiment.experiment_id,
                    score=score,
                )

                completed += 1

            except Exception:
                failed += 1

        total = completed + failed

        success_rate = (
            round(completed / total * 100.0, 2)
            if total
            else 0.0
        )

        return BatchRunSummary(
            total=total,
            completed=completed,
            failed=failed,
            success_rate=success_rate,
        )
