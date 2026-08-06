"""
Tests for the HAPT Batch Optimization Runner.
"""

from app.optimization.strategy_parameters import StrategyParameters
from app.research.batch_runner import (
    BatchOptimizationRunner,
    BatchRunSummary,
)
from app.research.experiment_manager import ExperimentManager


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


def test_empty_batch():
    """Running an empty batch should succeed."""

    manager = ExperimentManager()

    summary = BatchOptimizationRunner.run(manager)

    assert isinstance(summary, BatchRunSummary)
    assert summary.total == 0
    assert summary.completed == 0
    assert summary.failed == 0
    assert summary.success_rate == 0.0


def test_single_experiment():
    """One queued experiment should complete."""

    manager = ExperimentManager()

    manager.add(make_parameters())

    summary = BatchOptimizationRunner.run(manager)

    assert summary.total == 1
    assert summary.completed == 1
    assert summary.failed == 0
    assert summary.success_rate == 100.0
    assert manager.completed == 1


def test_multiple_experiments():
    """Multiple queued experiments should complete."""

    manager = ExperimentManager()

    for _ in range(5):
        manager.add(make_parameters())

    summary = BatchOptimizationRunner.run(manager)

    assert summary.total == 5
    assert summary.completed == 5
    assert manager.completed == 5


def test_custom_score_provider():
    """Custom score provider should be used."""

    manager = ExperimentManager()

    manager.add(make_parameters())

    summary = BatchOptimizationRunner.run(
        manager,
        score_provider=lambda exp: 87.5,
    )

    experiment = manager.experiments[0]

    assert summary.completed == 1
    assert experiment.score == 87.5


def test_failure_handling():
    """Exceptions should be counted as failures."""

    manager = ExperimentManager()

    manager.add(make_parameters())

    def failing_provider(_):
        raise RuntimeError("Failure")

    summary = BatchOptimizationRunner.run(
        manager,
        score_provider=failing_provider,
    )

    assert summary.total == 1
    assert summary.completed == 0
    assert summary.failed == 1
    assert summary.success_rate == 0.0


def test_success_rate():
    """Success rate should be calculated correctly."""

    manager = ExperimentManager()

    manager.add(make_parameters())
    manager.add(make_parameters())

    calls = 0

    def provider(_):
        nonlocal calls
        calls += 1
        if calls == 2:
            raise RuntimeError()
        return 95.0

    summary = BatchOptimizationRunner.run(
        manager,
        score_provider=provider,
    )

    assert summary.total == 2
    assert summary.completed == 1
    assert summary.failed == 1
    assert summary.success_rate == 50.0
