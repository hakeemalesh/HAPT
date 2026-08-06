"""
Tests for the HAPT Walk-Forward Validation.
"""

from app.optimization.optimization_result import OptimizationResult
from app.optimization.strategy_parameters import StrategyParameters
from app.optimization.walk_forward import (
    WalkForwardValidator,
    WalkForwardWindow,
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


def make_result(net_profit, win_rate):
    return OptimizationResult(
        parameters=make_parameters(),
        total_trades=100,
        net_profit=net_profit,
        win_rate=win_rate,
        profit_factor=2.0,
        expectancy=18.5,
        max_drawdown=250.0,
    )


def test_single_window():
    """One completed validation window."""

    windows = [
        WalkForwardWindow(
            0, 99,
            100, 149,
        )
    ]

    results = [
        make_result(500.0, 60.0)
    ]

    summary = WalkForwardValidator.validate(
        windows,
        results,
    )

    assert summary["windows"] == 1
    assert summary["completed"] is True


def test_average_values():
    """Average statistics should be calculated."""

    windows = [
        WalkForwardWindow(0, 99, 100, 149),
        WalkForwardWindow(100, 199, 200, 249),
    ]

    results = [
        make_result(500.0, 60.0),
        make_result(700.0, 70.0),
    ]

    summary = WalkForwardValidator.validate(
        windows,
        results,
    )

    assert summary["average_net_profit"] == 600.0
    assert summary["average_win_rate"] == 65.0


def test_partial_completion():
    """Validation should detect incomplete runs."""

    windows = [
        WalkForwardWindow(0, 99, 100, 149),
        WalkForwardWindow(100, 199, 200, 249),
    ]

    results = [
        make_result(500.0, 60.0),
    ]

    summary = WalkForwardValidator.validate(
        windows,
        results,
    )

    assert summary["windows"] == 1
    assert summary["completed"] is False


def test_empty_results():
    """Empty validation should return zeros."""

    windows = []

    results = []

    summary = WalkForwardValidator.validate(
        windows,
        results,
    )

    assert summary["windows"] == 0
    assert summary["average_net_profit"] == 0.0
    assert summary["average_win_rate"] == 0.0
    assert summary["completed"] is True
