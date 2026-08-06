"""
Tests for the HAPT Capital Allocation Engine.
"""

import pytest

from app.portfolio.capital_allocation import (
    AllocationPolicy,
    CapitalAllocationEngine,
    CapitalAllocationResult,
)


def test_equal_weight():
    result = CapitalAllocationEngine.equal_weight(
        total_capital=10000.0,
        strategy_count=4,
    )

    assert isinstance(result, CapitalAllocationResult)
    assert result.allocated_capital == 2500.0
    assert result.remaining_capital == 0.0
    assert result.policy == AllocationPolicy.EQUAL_WEIGHT


def test_fixed_amount():
    result = CapitalAllocationEngine.fixed_amount(
        total_capital=10000.0,
        amount=3000.0,
    )

    assert result.allocated_capital == 3000.0
    assert result.remaining_capital == 7000.0
    assert result.policy == AllocationPolicy.FIXED_AMOUNT


def test_percentage():
    result = CapitalAllocationEngine.percentage(
        total_capital=10000.0,
        percent=25.0,
    )

    assert result.allocated_capital == 2500.0
    assert result.remaining_capital == 7500.0
    assert result.policy == AllocationPolicy.PERCENTAGE


def test_invalid_strategy_count():
    with pytest.raises(ValueError):
        CapitalAllocationEngine.equal_weight(
            total_capital=10000.0,
            strategy_count=0,
        )


def test_invalid_fixed_amount():
    with pytest.raises(ValueError):
        CapitalAllocationEngine.fixed_amount(
            total_capital=10000.0,
            amount=15000.0,
        )


def test_invalid_fixed_amount_zero():
    with pytest.raises(ValueError):
        CapitalAllocationEngine.fixed_amount(
            total_capital=10000.0,
            amount=0.0,
        )


def test_invalid_percentage_zero():
    with pytest.raises(ValueError):
        CapitalAllocationEngine.percentage(
            total_capital=10000.0,
            percent=0.0,
        )


def test_invalid_percentage_over_100():
    with pytest.raises(ValueError):
        CapitalAllocationEngine.percentage(
            total_capital=10000.0,
            percent=120.0,
        )


def test_equal_weight_with_remainder():
    result = CapitalAllocationEngine.equal_weight(
        total_capital=10001.0,
        strategy_count=4,
    )

    assert result.allocated_capital == 2500.25
    assert result.remaining_capital == 0.0
