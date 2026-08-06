"""
Tests for the HAPT Slippage Engine.
"""

from app.pnl.slippage_engine import (
    SlippageEngine,
)


def test_mes_default_slippage():
    """MES default slippage."""

    assert (
        SlippageEngine.calculate("MES")
        == 1.25
    )


def test_mnq_default_slippage():
    """MNQ default slippage."""

    assert (
        SlippageEngine.calculate("MNQ")
        == 0.50
    )


def test_es_default_slippage():
    """ES default slippage."""

    assert (
        SlippageEngine.calculate("ES")
        == 12.50
    )


def test_nq_default_slippage():
    """NQ default slippage."""

    assert (
        SlippageEngine.calculate("NQ")
        == 5.00
    )


def test_multiple_mes_contracts():
    """Multiple MES contracts."""

    assert (
        SlippageEngine.calculate(
            "MES",
            quantity=4,
        )
        == 5.00
    )


def test_custom_slippage():
    """Custom slippage ticks."""

    assert (
        SlippageEngine.calculate(
            "MES",
            slippage_ticks=3,
        )
        == 3.75
    )


def test_multiple_contracts_and_ticks():
    """Multiple contracts with custom ticks."""

    assert (
        SlippageEngine.calculate(
            "ES",
            quantity=2,
            slippage_ticks=2,
        )
        == 50.00
    )
