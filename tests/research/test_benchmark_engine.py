"""
Tests for the HAPT Strategy Benchmark Engine.
"""

import pytest

from app.optimization.optimization_result import OptimizationResult
from app.optimization.strategy_parameters import StrategyParameters
from app.research.benchmark_engine import (
    BenchmarkEntry,
    StrategyBenchmarkEngine,
)


def make_result(
    net_profit,
    profit_factor,
    expectancy,
    win_rate,
    max_drawdown,
):
    params = StrategyParameters(
        instrument="MES",
        timeframe="5m",
        ema_fast=9,
        ema_slow=20,
        atr_period=14,
        atr_multiplier=2.0,
        risk_per_trade=30.0,
    )

    return OptimizationResult(
        parameters=params,
        total_trades=100,
        net_profit=net_profit,
        win_rate=win_rate,
        profit_factor=profit_factor,
        expectancy=expectancy,
        max_drawdown=max_drawdown,
    )


def make_entries():
    return [
        BenchmarkEntry(
            "Strategy A",
            make_result(1000, 1.5, 10, 55, 400),
        ),
        BenchmarkEntry(
            "Strategy B",
            make_result(3000, 2.4, 25, 65, 150),
        ),
        BenchmarkEntry(
            "Strategy C",
            make_result(2000, 1.9, 18, 60, 250),
        ),
    ]


def test_rank_by_net_profit():
    ranked = StrategyBenchmarkEngine.rank(make_entries())

    assert ranked[0].project_name == "Strategy B"
    assert ranked[1].project_name == "Strategy C"
    assert ranked[2].project_name == "Strategy A"


def test_rank_by_profit_factor():
    ranked = StrategyBenchmarkEngine.rank(
        make_entries(),
        metric="profit_factor",
    )

    assert ranked[0].result.profit_factor == 2.4


def test_rank_by_drawdown():
    ranked = StrategyBenchmarkEngine.rank(
        make_entries(),
        metric="max_drawdown",
    )

    assert ranked[0].result.max_drawdown == 150
    assert ranked[2].result.max_drawdown == 400


def test_winner():
    winner = StrategyBenchmarkEngine.winner(
        make_entries()
    )

    assert winner is not None
    assert winner.project_name == "Strategy B"


def test_empty_winner():
    assert (
        StrategyBenchmarkEngine.winner([])
        is None
    )


def test_invalid_metric():
    with pytest.raises(ValueError):
        StrategyBenchmarkEngine.rank(
            make_entries(),
            metric="invalid",
        )
