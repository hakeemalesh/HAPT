"""
Tests for the HAPT Trailing Stop Engine.
"""

from app.trade.trade import Trade
from app.trade.trailing_stop_engine import (
    TrailingStopEngine,
)


def test_long_trailing_stop_moves_up():
    """Long stop should move upward."""

    trade = Trade(
        symbol="MES",
        direction="LONG",
        quantity=1,
        entry_price=5000.00,
        stop_loss=4990.00,
    )

    updated = TrailingStopEngine.update(
        trade=trade,
        trail_distance=10.00,
        current_price=5015.00,
    )

    assert updated is True
    assert trade.stop_loss == 5005.00


def test_long_trailing_stop_does_not_move_down():
    """Long stop should never move lower."""

    trade = Trade(
        symbol="MES",
        direction="LONG",
        quantity=1,
        entry_price=5000.00,
        stop_loss=5005.00,
    )

    updated = TrailingStopEngine.update(
        trade=trade,
        trail_distance=10.00,
        current_price=5010.00,
    )

    assert updated is False
    assert trade.stop_loss == 5005.00


def test_short_trailing_stop_moves_down():
    """Short stop should move downward."""

    trade = Trade(
        symbol="MNQ",
        direction="SHORT",
        quantity=1,
        entry_price=22000.00,
        stop_loss=22020.00,
    )

    updated = TrailingStopEngine.update(
        trade=trade,
        trail_distance=10.00,
        current_price=21990.00,
    )

    assert updated is True
    assert trade.stop_loss == 22000.00


def test_short_trailing_stop_does_not_move_up():
    """Short stop should never move higher."""

    trade = Trade(
        symbol="MNQ",
        direction="SHORT",
        quantity=1,
        entry_price=22000.00,
        stop_loss=22000.00,
    )

    updated = TrailingStopEngine.update(
        trade=trade,
        trail_distance=10.00,
        current_price=21995.00,
    )

    assert updated is False
    assert trade.stop_loss == 22000.00


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

    updated = TrailingStopEngine.update(
        trade=trade,
        trail_distance=10.00,
        current_price=5020.00,
    )

    assert updated is False
    assert trade.stop_loss == 4990.00


def test_trade_without_stop_loss():
    """Trades without stop loss should be ignored."""

    trade = Trade(
        symbol="MES",
        direction="LONG",
        quantity=1,
        entry_price=5000.00,
    )

    updated = TrailingStopEngine.update(
        trade=trade,
        trail_distance=10.00,
        current_price=5020.00,
    )

    assert updated is False
    assert trade.stop_loss is None
