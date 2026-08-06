"""
Tests for the HAPT Stop Loss Engine.
"""

from datetime import datetime

from app.trade.stop_loss_engine import StopLossEngine
from app.trade.trade import Trade


def test_long_stop_loss_hit():
    """Long trade should close when low reaches stop."""

    trade = Trade(
        symbol="MES",
        direction="LONG",
        quantity=1,
        entry_price=5000.00,
        stop_loss=4995.00,
    )

    candle = {
        "high": 5002.00,
        "low": 4994.75,
        "close": 4996.00,
        "timestamp": datetime(2026, 8, 1, 10, 0),
    }

    assert StopLossEngine.evaluate(trade, candle) is True
    assert trade.status == "CLOSED"
    assert trade.exit_price == 4995.00
    assert trade.exit_reason == "Stop Loss"


def test_long_stop_loss_not_hit():
    """Long trade should remain open."""

    trade = Trade(
        symbol="MES",
        direction="LONG",
        quantity=1,
        entry_price=5000.00,
        stop_loss=4995.00,
    )

    candle = {
        "high": 5003.00,
        "low": 4998.00,
        "close": 5002.00,
        "timestamp": datetime(2026, 8, 1, 10, 5),
    }

    assert StopLossEngine.evaluate(trade, candle) is False
    assert trade.status == "OPEN"
    assert trade.exit_price is None


def test_short_stop_loss_hit():
    """Short trade should close when high reaches stop."""

    trade = Trade(
        symbol="MNQ",
        direction="SHORT",
        quantity=1,
        entry_price=22000.00,
        stop_loss=22020.00,
    )

    candle = {
        "high": 22021.00,
        "low": 21980.00,
        "close": 22015.00,
        "timestamp": datetime(2026, 8, 1, 11, 0),
    }

    assert StopLossEngine.evaluate(trade, candle) is True
    assert trade.status == "CLOSED"
    assert trade.exit_price == 22020.00
    assert trade.exit_reason == "Stop Loss"


def test_closed_trade_is_ignored():
    """Closed trades should not be modified."""

    trade = Trade(
        symbol="MES",
        direction="LONG",
        quantity=1,
        entry_price=5000.00,
        stop_loss=4995.00,
        status="CLOSED",
    )

    candle = {
        "high": 5001.00,
        "low": 4990.00,
        "close": 4992.00,
        "timestamp": datetime(2026, 8, 1, 10, 0),
    }

    assert StopLossEngine.evaluate(trade, candle) is False


def test_trade_without_stop_loss():
    """Trades without a stop loss should be ignored."""

    trade = Trade(
        symbol="MES",
        direction="LONG",
        quantity=1,
        entry_price=5000.00,
    )

    candle = {
        "high": 5001.00,
        "low": 4990.00,
        "close": 4992.00,
        "timestamp": datetime(2026, 8, 1, 10, 0),
    }

    assert StopLossEngine.evaluate(trade, candle) is False
    assert trade.status == "OPEN"
