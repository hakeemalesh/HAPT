"""
Tests for the HAPT Futures Tick Value Engine.
"""

import pytest

from app.pnl.tick_value_engine import TickValueEngine


def test_mes_tick_size():
    """MES tick size."""

    assert (
        TickValueEngine.get_tick_size("MES")
        == 0.25
    )


def test_mes_tick_value():
    """MES tick value."""

    assert (
        TickValueEngine.get_tick_value("MES")
        == 1.25
    )


def test_es_tick_value():
    """ES tick value."""

    assert (
        TickValueEngine.get_tick_value("ES")
        == 12.50
    )


def test_mnq_tick_value():
    """MNQ tick value."""

    assert (
        TickValueEngine.get_tick_value("MNQ")
        == 0.50
    )


def test_nq_tick_value():
    """NQ tick value."""

    assert (
        TickValueEngine.get_tick_value("NQ")
        == 5.00
    )


def test_tick_calculation():
    """One point equals four ticks."""

    ticks = TickValueEngine.calculate_ticks(
        symbol="MES",
        entry_price=5000.00,
        exit_price=5001.00,
    )

    assert ticks == 4.0


def test_negative_tick_calculation():
    """Down move should produce negative ticks."""

    ticks = TickValueEngine.calculate_ticks(
        symbol="MES",
        entry_price=5001.00,
        exit_price=5000.00,
    )

    assert ticks == -4.0


def test_invalid_tick_size_symbol():
    """Unknown symbol should raise ValueError."""

    with pytest.raises(ValueError):
        TickValueEngine.get_tick_size("ABC")


def test_invalid_tick_value_symbol():
    """Unknown symbol should raise ValueError."""

    with pytest.raises(ValueError):
        TickValueEngine.get_tick_value("ABC")


def test_invalid_tick_calculation_symbol():
    """Unknown symbol should raise ValueError."""

    with pytest.raises(ValueError):
        TickValueEngine.calculate_ticks(
            symbol="ABC",
            entry_price=100,
            exit_price=101,
        )
