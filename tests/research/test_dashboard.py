"""
Tests for the HAPT Research Dashboard.
"""

from app.optimization.optimization_result import OptimizationResult
from app.optimization.strategy_parameters import StrategyParameters
from app.research.benchmark_engine import BenchmarkEntry
from app.research.dashboard import ResearchDashboard
from app.research.experiment_manager import ExperimentManager
from app.research.repository import ResearchRepository
from app.research.research_project import ResearchProject


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


def make_result():
    return OptimizationResult(
        parameters=make_parameters(),
        total_trades=100,
        net_profit=5000.0,
        win_rate=62.0,
        profit_factor=2.3,
        expectancy=31.5,
        max_drawdown=240.0,
    )


def make_project():
    return ResearchProject(
        name="MES Research",
        objective="EMA Optimization",
        instrument="MES",
        timeframe="5m",
        total_experiments=10,
        completed_experiments=5,
    )


def test_dashboard_creation():
    project = make_project()

    manager = ExperimentManager()

    repository = ResearchRepository()
    repository.save(project)

    dashboard = ResearchDashboard.build(
        project=project,
        experiments=manager,
        repository=repository,
        benchmark_entries=[],
    )

    assert dashboard["project_name"] == "MES Research"
    assert dashboard["status"] == "CREATED"
    assert dashboard["progress"] == 50.0
    assert dashboard["repository_projects"] == 1


def test_dashboard_with_benchmark():
    project = make_project()

    manager = ExperimentManager()

    repository = ResearchRepository()

    entry = BenchmarkEntry(
        "Winner",
        make_result(),
    )

    dashboard = ResearchDashboard.build(
        project=project,
        experiments=manager,
        repository=repository,
        benchmark_entries=[entry],
    )

    assert dashboard["best_project"] == "Winner"
    assert dashboard["best_result"] == 5000.0


def test_dashboard_without_benchmark():
    project = make_project()

    manager = ExperimentManager()

    repository = ResearchRepository()

    dashboard = ResearchDashboard.build(
        project=project,
        experiments=manager,
        repository=repository,
        benchmark_entries=[],
    )

    assert dashboard["best_project"] is None
    assert dashboard["best_result"] is None


def test_dashboard_experiment_counts():
    manager = ExperimentManager()

    manager.add(make_parameters())
    manager.add(make_parameters())

    manager.start(1)
    manager.complete(1, 91.0)

    project = make_project()

    dashboard = ResearchDashboard.build(
        project=project,
        experiments=manager,
        repository=ResearchRepository(),
        benchmark_entries=[],
    )

    assert dashboard["completed"] == 1
    assert dashboard["queued"] == 1
    assert dashboard["running"] == 0


def test_dashboard_timestamp():
    dashboard = ResearchDashboard.build(
        project=make_project(),
        experiments=ExperimentManager(),
        repository=ResearchRepository(),
        benchmark_entries=[],
    )

    assert dashboard["generated_at"] is not None
