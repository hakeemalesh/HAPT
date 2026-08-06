"""
Tests for the HAPT Strategy Ranking Engine.
"""

import pytest

from app.optimization.optimization_result import OptimizationResult
from app.optimization.strategy_parameters import StrategyParameters
from app.optimization.strategy_ranking import StrategyRanking


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


def test_rank_by_net_profit():
    results = [
        make_result(1000, 1.5, 10, 55, 300),
        make_result(3000, 2.0, 20, 60, 250),
        make_result(2000, 1.8, 15, 58, 275),
    ]

    ranked = StrategyRanking.rank(results)

    assert ranked[0].net_profit == 3000
    assert ranked[1].net_profit == 2000
    assert ranked[2].net_profit == 1000


def test_rank_by_profit_factor():
    results = [
        make_result(1000, 1.5, 10, 55, 300),
        make_result(3000, 2.5, 20, 60, 250),
        make_result(2000, 1.8, 15, 58, 275),
    ]

    ranked = StrategyRanking.rank(
        results,
        metric="profit_factor",
    )

    assert ranked[0].profit_factor == 2.5


def test_rank_by_expectancy():
    results = [
        make_result(1000, 1.5, 10, 55, 300),
        make_result(3000, 2.0, 25, 60, 250),
    ]

    ranked = StrategyRanking.rank(
        results,
        metric="expectancy",
    )

    assert ranked[0].expectancy == 25


def test_rank_by_win_rate():
    results = [
        make_result(1000, 1.5, 10, 52, 300),
        make_result(3000, 2.0, 20, 68, 250),
    ]

    ranked = StrategyRanking.rank(
        results,
        metric="win_rate",
    )

    assert ranked[0].win_rate == 68


def test_rank_by_drawdown():
    results = [
        make_result(1000, 1.5, 10, 55, 400),
        make_result(3000, 2.0, 20, 60, 150),
        make_result(2000, 1.8, 15, 58, 250),
    ]

    ranked = StrategyRanking.rank(
        results,
        metric="max_drawdown",
    )

    assert ranked[0].max_drawdown == 150
    assert ranked[1].max_drawdown == 250
    assert ranked[2].max_drawdown == 400


def test_invalid_metric():
    results = []

    with pytest.raises(ValueError):
        StrategyRanking.rank(
            results,
            metric="invalid_metric",
        )
