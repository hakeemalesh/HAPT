"""
Tests for the HAPT Break-even Stop Engine.
"""

from app.trade.breakeven_engine import BreakEvenEngine
from app.trade.trade import Trade


def test_long_break_even_triggered():
    """Long trade should move stop to entry."""

    trade = Trade(
        symbol="MES",
        direction="LONG",
        quantity=1,
        entry_price=5000.00,
        stop_loss=4990.00,
    )

    updated = BreakEvenEngine.update(
        trade=trade,
        trigger_distance=10.00,
        current_price=5012.00,
    )

    assert updated is True
    assert trade.stop_loss == 5000.00


def test_long_break_even_not_triggered():
    """Long trade should keep original stop."""

    trade = Trade(
        symbol="MES",
        direction="LONG",
        quantity=1,
        entry_price=5000.00,
        stop_loss=4990.00,
    )

    updated = BreakEvenEngine.update(
        trade=trade,
        trigger_distance=10.00,
        current_price=5008.00,
    )

    assert updated is False
    assert trade.stop_loss == 4990.00


def test_short_break_even_triggered():
    """Short trade should move stop to entry."""

    trade = Trade(
        symbol="MNQ",
        direction="SHORT",
        quantity=1,
        entry_price=22000.00,
        stop_loss=22010.00,
    )

    updated = BreakEvenEngine.update(
        trade=trade,
        trigger_distance=10.00,
        current_price=21988.00,
    )

    assert updated is True
    assert trade.stop_loss == 22000.00


def test_short_break_even_not_triggered():
    """Short trade should keep original stop."""

    trade = Trade(
        symbol="MNQ",
        direction="SHORT",
        quantity=1,
        entry_price=22000.00,
        stop_loss=22010.00,
    )

    updated = BreakEvenEngine.update(
        trade=trade,
        trigger_distance=10.00,
        current_price=21995.00,
    )

    assert updated is False
    assert trade.stop_loss == 22010.00


def test_closed_trade_not_updated():
    """Closed trades should be ignored."""

    trade = Trade(
        symbol="MES",
        direction="LONG",
        quantity=1,
        entry_price=5000.00,
        stop_loss=4990.00,
        status="CLOSED",
    )

    updated = BreakEvenEngine.update(
        trade=trade,
        trigger_distance=10.00,
        current_price=5020.00,
    )

    assert updated is False
    assert trade.stop_loss == 4990.00


def test_trade_without_stop_loss():
    """Trades without a stop-loss should be ignored."""

    trade = Trade(
        symbol="MES",
        direction="LONG",
        quantity=1,
        entry_price=5000.00,
    )

    updated = BreakEvenEngine.update(
        trade=trade,
        trigger_distance=10.00,
        current_price=5020.00,
    )

    assert updated is False
    assert trade.stop_loss is None
