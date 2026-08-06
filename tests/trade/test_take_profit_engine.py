"""
Tests for the HAPT Take Profit Engine.
"""

from datetime import datetime

from app.trade.take_profit_engine import (
    TakeProfitEngine,
)
from app.trade.trade import Trade


def test_long_take_profit_hit():
    """Long trade should close at take profit."""

    trade = Trade(
        symbol="MES",
        direction="LONG",
        quantity=1,
        entry_price=5000.00,
        take_profit=5010.00,
    )

    candle = {
        "high": 5011.00,
        "low": 4999.00,
        "close": 5008.00,
        "timestamp": datetime(2026, 8, 1, 10, 0),
    }

    assert (
        TakeProfitEngine.evaluate(
            trade,
            candle,
        )
        is True
    )

    assert trade.status == "CLOSED"
    assert trade.exit_price == 5010.00
    assert trade.exit_reason == "Take Profit"


def test_long_take_profit_not_hit():
    """Long trade should remain open."""

    trade = Trade(
        symbol="MES",
        direction="LONG",
        quantity=1,
        entry_price=5000.00,
        take_profit=5010.00,
    )

    candle = {
        "high": 5008.00,
        "low": 4999.00,
        "close": 5007.00,
        "timestamp": datetime(2026, 8, 1, 10, 5),
    }

    assert (
        TakeProfitEngine.evaluate(
            trade,
            candle,
        )
        is False
    )

    assert trade.status == "OPEN"
    assert trade.exit_price is None


def test_short_take_profit_hit():
    """Short trade should close at take profit."""

    trade = Trade(
        symbol="MNQ",
        direction="SHORT",
        quantity=1,
        entry_price=22000.00,
        take_profit=21980.00,
    )

    candle = {
        "high": 22005.00,
        "low": 21979.00,
        "close": 21982.00,
        "timestamp": datetime(2026, 8, 1, 11, 0),
    }

    assert (
        TakeProfitEngine.evaluate(
            trade,
            candle,
        )
        is True
    )

    assert trade.status == "CLOSED"
    assert trade.exit_price == 21980.00
    assert trade.exit_reason == "Take Profit"


def test_closed_trade_is_ignored():
    """Closed trades should not be modified."""

    trade = Trade(
        symbol="MES",
        direction="LONG",
        quantity=1,
        entry_price=5000.00,
        take_profit=5010.00,
        status="CLOSED",
    )

    candle = {
        "high": 5012.00,
        "low": 4998.00,
        "close": 5011.00,
        "timestamp": datetime(2026, 8, 1, 10, 0),
    }

    assert (
        TakeProfitEngine.evaluate(
            trade,
            candle,
        )
        is False
    )


def test_trade_without_take_profit():
    """Trades without take profit should remain open."""

    trade = Trade(
        symbol="MES",
        direction="LONG",
        quantity=1,
        entry_price=5000.00,
    )

    candle = {
        "high": 5015.00,
        "low": 4998.00,
        "close": 5010.00,
        "timestamp": datetime(2026, 8, 1, 10, 0),
    }

    assert (
        TakeProfitEngine.evaluate(
            trade,
            candle,
        )
        is False
    )

    assert trade.status == "OPEN"
