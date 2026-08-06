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
    assert result["gross_pnl"] == 5.00
    assert result["commission"] == 1.24
    assert result["slippage"] == 1.25
    assert result["net_pnl"] == 2.51


def test_mes_long_loss():
    """MES long trade loss."""

    result = PnLCalculator.calculate(
        symbol="MES",
        entry_price=5001.00,
        exit_price=5000.00,
    )

    assert result["gross_pnl"] == -5.00
    assert result["commission"] == 1.24
    assert result["slippage"] == 1.25
    assert result["net_pnl"] == -7.49


def test_mes_short_profit():
    """MES short trade profit."""

    result = PnLCalculator.calculate(
        symbol="MES",
        entry_price=5001.00,
        exit_price=5000.00,
        direction="SHORT",
    )

    assert result["gross_pnl"] == 5.00
    assert result["commission"] == 1.24
    assert result["slippage"] == 1.25
    assert result["net_pnl"] == 2.51


def test_mes_short_loss():
    """MES short trade loss."""

    result = PnLCalculator.calculate(
        symbol="MES",
        entry_price=5000.00,
        exit_price=5001.00,
        direction="SHORT",
    )

    assert result["gross_pnl"] == -5.00
    assert result["commission"] == 1.24
    assert result["slippage"] == 1.25
    assert result["net_pnl"] == -7.49


def test_multiple_contracts():
    """Multiple contracts scale correctly."""

    result = PnLCalculator.calculate(
        symbol="MES",
        entry_price=5000.00,
        exit_price=5001.00,
        quantity=4,
    )

    assert result["gross_pnl"] == 20.00
    assert result["commission"] == 4.96
    assert result["slippage"] == 5.00
    assert result["net_pnl"] == 10.04


def test_es_trade():
    """ES trade."""

    result = PnLCalculator.calculate(
        symbol="ES",
        entry_price=6000.00,
        exit_price=6001.00,
    )

    assert result["gross_pnl"] == 50.00
    assert result["commission"] == 2.48
    assert result["slippage"] == 12.50
    assert result["net_pnl"] == 35.02


def test_mnq_trade():
    """MNQ trade."""

    result = PnLCalculator.calculate(
        symbol="MNQ",
        entry_price=22000.00,
        exit_price=22001.00,
    )

    assert result["gross_pnl"] == 2.00
    assert result["commission"] == 1.24
    assert result["slippage"] == 0.50
    assert result["net_pnl"] == 0.26


def test_nq_trade():
    """NQ trade."""

    result = PnLCalculator.calculate(
        symbol="NQ",
        entry_price=22000.00,
        exit_price=22001.00,
    )

    assert result["gross_pnl"] == 20.00
    assert result["commission"] == 2.48
    assert result["slippage"] == 5.00
    assert result["net_pnl"] == 12.52


def test_invalid_direction():
    """Invalid direction."""

    with pytest.raises(ValueError):
        PnLCalculator.calculate(
            symbol="MES",
            entry_price=100,
            exit_price=101,
            direction="BUY",
        )


def test_invalid_symbol():
    """Unknown symbol."""

    with pytest.raises(ValueError):
        PnLCalculator.calculate(
            symbol="ABC",
            entry_price=100,
            exit_price=101,
        )
