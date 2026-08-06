"""
Tests for the HAPT Parameter Grid Generator.
"""

from app.optimization.grid_generator import GridGenerator
from app.optimization.strategy_parameters import StrategyParameters


def test_single_combination():
    """Generate one valid parameter set."""

    grid = GridGenerator.generate(
        instrument="MES",
        timeframe="5m",
        ema_fast_values=[9],
        ema_slow_values=[20],
        atr_period_values=[14],
        atr_multiplier_values=[2.0],
        risk_per_trade=30.0,
    )

    assert len(grid) == 1

    params = grid[0]

    assert isinstance(params, StrategyParameters)
    assert params.ema_fast == 9
    assert params.ema_slow == 20
    assert params.atr_period == 14
    assert params.atr_multiplier == 2.0


def test_multiple_combinations():
    """Generate every valid combination."""

    grid = GridGenerator.generate(
        instrument="MES",
        timeframe="5m",
        ema_fast_values=[5, 10],
        ema_slow_values=[20, 30],
        atr_period_values=[14],
        atr_multiplier_values=[1.5, 2.0],
        risk_per_trade=30.0,
    )

    assert len(grid) == 8


def test_invalid_ema_pairs_are_filtered():
    """Fast EMA must always be smaller than slow EMA."""

    grid = GridGenerator.generate(
        instrument="MES",
        timeframe="5m",
        ema_fast_values=[20],
        ema_slow_values=[10, 20],
        atr_period_values=[14],
        atr_multiplier_values=[2.0],
        risk_per_trade=30.0,
    )

    assert grid == []


def test_optional_values_are_propagated():
    """Optional parameters should appear in every result."""

    grid = GridGenerator.generate(
        instrument="MNQ",
        timeframe="15m",
        ema_fast_values=[8],
        ema_slow_values=[21],
        atr_period_values=[10],
        atr_multiplier_values=[1.5],
        risk_per_trade=50.0,
        session="POWER_HOUR",
        allow_long=False,
        allow_short=True,
    )

    params = grid[0]

    assert params.instrument == "MNQ"
    assert params.timeframe == "15m"
    assert params.session == "POWER_HOUR"
    assert params.allow_long is False
    assert params.allow_short is True


def test_every_result_is_strategy_parameters():
    """Every generated item should be a StrategyParameters instance."""

    grid = GridGenerator.generate(
        instrument="MES",
        timeframe="5m",
        ema_fast_values=[5, 10],
        ema_slow_values=[20],
        atr_period_values=[14],
        atr_multiplier_values=[2.0],
        risk_per_trade=30.0,
    )

    assert all(
        isinstance(item, StrategyParameters)
        for item in grid
    )
