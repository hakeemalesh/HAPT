"""
Tests for the HAPT Commission Engine.
"""

import pytest

from app.pnl.commission_engine import CommissionEngine


def test_mes_commission():
    """MES commission."""

    assert (
        CommissionEngine.calculate("MES")
        == 1.24
    )


def test_mnq_commission():
    """MNQ commission."""

    assert (
        CommissionEngine.calculate("MNQ")
        == 1.24
    )


def test_es_commission():
    """ES commission."""

    assert (
        CommissionEngine.calculate("ES")
        == 2.48
    )


def test_nq_commission():
    """NQ commission."""

    assert (
        CommissionEngine.calculate("NQ")
        == 2.48
    )


def test_multiple_contracts_mes():
    """Multiple MES contracts."""

    assert (
        CommissionEngine.calculate(
            "MES",
            quantity=4,
        )
        == 4.96
    )


def test_multiple_contracts_es():
    """Multiple ES contracts."""

    assert (
        CommissionEngine.calculate(
            "ES",
            quantity=3,
        )
        == 7.44
    )


def test_invalid_symbol():
    """Unknown symbol should raise ValueError."""

    with pytest.raises(ValueError):
        CommissionEngine.calculate("ABC")
