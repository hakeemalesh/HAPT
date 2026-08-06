"""
Tests for the HAPT Strategy Parameter Model.
"""

from dataclasses import FrozenInstanceError

import pytest

from app.optimization.strategy_parameters import StrategyParameters


def test_create_strategy_parameters():
    """StrategyParameters should store values correctly."""

    params = StrategyParameters(
        instrument="MES",
        timeframe="5m",
        ema_fast=9,
        ema_slow=20,
        atr_period=14,
        atr_multiplier=2.0,
        risk_per_trade=30.0,
    )

    assert params.instrument == "MES"
    assert params.timeframe == "5m"
    assert params.ema_fast == 9
    assert params.ema_slow == 20
    assert params.atr_period == 14
    assert params.atr_multiplier == 2.0
    assert params.risk_per_trade == 30.0
    assert params.session == "REGULAR"
    assert params.allow_long is True
    assert params.allow_short is True


def test_custom_optional_values():
    """Optional values should override defaults."""

    params = StrategyParameters(
        instrument="MNQ",
        timeframe="15m",
        ema_fast=8,
        ema_slow=21,
        atr_period=10,
        atr_multiplier=1.5,
        risk_per_trade=50.0,
        session="POWER_HOUR",
        allow_long=False,
        allow_short=True,
    )

    assert params.session == "POWER_HOUR"
    assert params.allow_long is False
    assert params.allow_short is True


def test_parameters_are_immutable():
    """Frozen dataclass should reject modification."""

    params = StrategyParameters(
        instrument="MES",
        timeframe="5m",
        ema_fast=9,
        ema_slow=20,
        atr_period=14,
        atr_multiplier=2.0,
        risk_per_trade=30.0,
    )

    with pytest.raises(FrozenInstanceError):
        params.ema_fast = 12
