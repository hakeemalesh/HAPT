"""
Tests for the HAPT Partial Profit Engine.
"""

from app.trade.partial_profit_engine import (
    PartialProfitEngine,
)
from app.trade.trade import Trade


def test_long_partial_profit():
    """Long trade should scale out."""

    trade = Trade(
        symbol="MES",
        direction="LONG",
        quantity=2,
        entry_price=5000.00,
    )

    executed = PartialProfitEngine.execute(
        trade=trade,
        target_price=5010.00,
        exit_quantity=1,
        current_price=5012.00,
    )

    assert executed is True
    assert trade.quantity == 1
    assert trade.status == "OPEN"


def test_short_partial_profit():
    """Short trade should scale out."""

    trade = Trade(
        symbol="MNQ",
        direction="SHORT",
        quantity=3,
        entry_price=22000.00,
    )

    executed = PartialProfitEngine.execute(
        trade=trade,
        target_price=21980.00,
        exit_quantity=1,
        current_price=21975.00,
    )

    assert executed is True
    assert trade.quantity == 2
    assert trade.status == "OPEN"


def test_target_not_reached():
    """Trade should remain unchanged."""

    trade = Trade(
        symbol="MES",
        direction="LONG",
        quantity=2,
        entry_price=5000.00,
    )

    executed = PartialProfitEngine.execute(
        trade=trade,
        target_price=5010.00,
        exit_quantity=1,
        current_price=5008.00,
    )

    assert executed is False
    assert trade.quantity == 2


def test_invalid_exit_quantity_zero():
    """Exit quantity must be positive."""

    trade = Trade(
        symbol="MES",
        direction="LONG",
        quantity=2,
        entry_price=5000.00,
    )

    executed = PartialProfitEngine.execute(
        trade=trade,
        target_price=5010.00,
        exit_quantity=0,
        current_price=5012.00,
    )

    assert executed is False
    assert trade.quantity == 2


def test_invalid_exit_quantity_too_large():
    """Cannot exit the full position."""

    trade = Trade(
        symbol="MES",
        direction="LONG",
        quantity=2,
        entry_price=5000.00,
    )

    executed = PartialProfitEngine.execute(
        trade=trade,
        target_price=5010.00,
        exit_quantity=2,
        current_price=5012.00,
    )

    assert executed is False
    assert trade.quantity == 2


def test_closed_trade():
    """Closed trades should be ignored."""

    trade = Trade(
        symbol="MES",
        direction="LONG",
        quantity=2,
        entry_price=5000.00,
        status="CLOSED",
    )

    executed = PartialProfitEngine.execute(
        trade=trade,
        target_price=5010.00,
        exit_quantity=1,
        current_price=5015.00,
    )

    assert executed is False
    assert trade.quantity == 2


def test_invalid_direction():
    """Invalid directions should be rejected."""

    trade = Trade(
        symbol="MES",
        direction="INVALID",
        quantity=2,
        entry_price=5000.00,
    )

    executed = PartialProfitEngine.execute(
        trade=trade,
        target_price=5010.00,
        exit_quantity=1,
        current_price=5015.00,
    )

    assert executed is False
    assert trade.quantity == 2
