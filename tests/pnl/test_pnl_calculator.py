"""
Tests for the HAPT Profit & Loss Calculator.
"""

import pytest

from app.pnl.pnl_calculator import PnLCalculator


def test_mes_long_profit():
    """MES long trade profit."""

    result = PnLCalculator.calculate(
        symbol="MES",
        entry_price=5000.00,
        exit_price=5001.00,
    )

    assert result["ticks"] == 4.0
    assert result["gross_pnl"] == 5.0


def test_mes_long_loss():
    """MES long trade loss."""

    result = PnLCalculator.calculate(
        symbol="MES",
        entry_price=5001.00,
        exit_price=5000.00,
    )

    assert result["ticks"] == -4.0
    assert result["gross_pnl"] == -5.0


def test_mes_short_profit():
    """MES short trade profit."""

    result = PnLCalculator.calculate(
        symbol="MES",
        entry_price=5001.00,
        exit_price=5000.00,
        direction="SHORT",
    )

    assert result["ticks"] == 4.0
    assert result["gross_pnl"] == 5.0


def test_mes_short_loss():
    """MES short trade loss."""

    result = PnLCalculator.calculate(
        symbol="MES",
        entry_price=5000.00,
        exit_price=5001.00,
        direction="SHORT",
    )

    assert result["ticks"] == -4.0
    assert result["gross_pnl"] == -5.0


def test_multiple_contracts():
    """Multiple contracts should scale P&L."""

    result = PnLCalculator.calculate(
        symbol="MES",
        entry_price=5000.00,
        exit_price=5001.00,
        quantity=4,
    )

    assert result["gross_pnl"] == 20.0


def test_es_tick_value():
    """ES should use correct tick value."""

    result = PnLCalculator.calculate(
        symbol="ES",
        entry_price=6000.00,
        exit_price=6001.00,
    )

    assert result["gross_pnl"] == 50.0


def test_mnq_tick_value():
    """MNQ should use correct tick value."""

    result = PnLCalculator.calculate(
        symbol="MNQ",
        entry_price=22000.00,
        exit_price=22001.00,
    )

    assert result["gross_pnl"] == 2.0


def test_nq_tick_value():
    """NQ should use correct tick value."""

    result = PnLCalculator.calculate(
        symbol="NQ",
        entry_price=22000.00,
        exit_price=22001.00,
    )

    assert result["gross_pnl"] == 20.0


def test_invalid_direction():
    """Invalid direction should raise ValueError."""

    with pytest.raises(ValueError):
        PnLCalculator.calculate(
            symbol="MES",
            entry_price=100,
            exit_price=101,
            direction="BUY",
        )


def test_invalid_symbol():
    """Unknown symbol should raise ValueError."""

    with pytest.raises(ValueError):
        PnLCalculator.calculate(
            symbol="ABC",
            entry_price=100,
            exit_price=101,
        )
