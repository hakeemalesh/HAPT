"""
Tests for the HAPT Experiment Manager.
"""

from app.optimization.strategy_parameters import StrategyParameters
from app.research.experiment_manager import (
    ExperimentManager,
    ResearchExperiment,
)


def make_parameters():
    return StrategyParameters(
        instrument="MES",
        timeframe="5m",
        ema_fast=9,
        ema_slow=20,
        atr_period=14,
        atr_multiplier=2.0,
        risk_per_trade=30.0,
    )


def test_add_experiment():
    """Adding an experiment should create experiment #1."""

    manager = ExperimentManager()

    experiment = manager.add(make_parameters())

    assert isinstance(experiment, ResearchExperiment)
    assert experiment.experiment_id == 1
    assert experiment.status == "QUEUED"
    assert manager.queued == 1


def test_sequential_ids():
    """Experiment IDs should increase sequentially."""

    manager = ExperimentManager()

    manager.add(make_parameters())
    second = manager.add(make_parameters())

    assert second.experiment_id == 2


def test_start_experiment():
    """Starting an experiment should update its status."""

    manager = ExperimentManager()

    manager.add(make_parameters())
    manager.start(1)

    experiment = manager.experiments[0]

    assert experiment.status == "RUNNING"
    assert experiment.started_at is not None
    assert manager.running == 1
    assert manager.queued == 0


def test_complete_experiment():
    """Completing an experiment should record its score."""

    manager = ExperimentManager()

    manager.add(make_parameters())
    manager.start(1)
    manager.complete(1, score=95.5)

    experiment = manager.experiments[0]

    assert experiment.status == "COMPLETED"
    assert experiment.score == 95.5
    assert experiment.completed_at is not None
    assert manager.completed == 1
    assert manager.running == 0


def test_multiple_status_counts():
    """Status counters should reflect mixed experiment states."""

    manager = ExperimentManager()

    manager.add(make_parameters())
    manager.add(make_parameters())
    manager.add(make_parameters())

    manager.start(1)
    manager.complete(1, 88.0)
    manager.start(2)

    assert manager.completed == 1
    assert manager.running == 1
    assert manager.queued == 1
