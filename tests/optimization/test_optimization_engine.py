"""
Tests for the HAPT Optimization Engine.
"""

from app.optimization.optimization_engine import OptimizationEngine
from app.optimization.optimization_result import OptimizationResult
from app.optimization.strategy_parameters import StrategyParameters


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


def test_evaluate_returns_result():
    """Engine should return an OptimizationResult."""

    result = OptimizationEngine.evaluate(
        parameters=make_parameters(),
        total_trades=120,
        net_profit=2450.0,
        win_rate=61.5,
        profit_factor=2.1,
        expectancy=20.4,
        max_drawdown=320.0,
    )

    assert isinstance(result, OptimizationResult)


def test_result_values_are_preserved():
    """All supplied values should be preserved."""

    params = make_parameters()

    result = OptimizationEngine.evaluate(
        parameters=params,
        total_trades=120,
        net_profit=2450.0,
        win_rate=61.5,
        profit_factor=2.1,
        expectancy=20.4,
        max_drawdown=320.0,
    )

    assert result.parameters == params
    assert result.total_trades == 120
    assert result.net_profit == 2450.0
    assert result.win_rate == 61.5
    assert result.profit_factor == 2.1
    assert result.expectancy == 20.4
    assert result.max_drawdown == 320.0
