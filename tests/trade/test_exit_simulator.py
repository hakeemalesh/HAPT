"""
Integration tests for the HAPT Exit Simulator.
"""

from datetime import datetime

from app.trade.exit_simulator import ExitSimulator
from app.trade.trade import Trade


def test_take_profit_closes_trade():
    """Take profit should close the trade."""

    trade = Trade(
        symbol="MES",
        direction="LONG",
        quantity=1,
        entry_price=5000.00,
        stop_loss=4990.00,
        take_profit=5010.00,
    )

    candle = {
        "high": 5012.00,
        "low": 4998.00,
        "close": 5011.00,
        "timestamp": datetime(2026, 8, 1, 10, 0),
    }

    ExitSimulator.process_candle(
        trade,
        candle,
    )

    assert trade.status == "CLOSED"
    assert trade.exit_reason == "Take Profit"
    assert trade.exit_price == 5010.00


def test_stop_loss_closes_trade():
    """Stop loss should close the trade."""

    trade = Trade(
        symbol="MES",
        direction="LONG",
        quantity=1,
        entry_price=5000.00,
        stop_loss=4990.00,
        take_profit=5010.00,
    )

    candle = {
        "high": 5002.00,
        "low": 4989.00,
        "close": 4990.00,
        "timestamp": datetime(2026, 8, 1, 10, 5),
    }

    ExitSimulator.process_candle(
        trade,
        candle,
    )

    assert trade.status == "CLOSED"
    assert trade.exit_reason == "Stop Loss"


def test_break_even_moves_stop():
    """Break-even engine should update stop."""

    trade = Trade(
        symbol="MES",
        direction="LONG",
        quantity=1,
        entry_price=5000.00,
        stop_loss=4990.00,
    )

    candle = {
        "high": 5015.00,
        "low": 5008.00,
        "close": 5012.00,
        "timestamp": datetime(2026, 8, 1, 10, 10),
    }

    ExitSimulator.process_candle(
        trade,
        candle,
        break_even_trigger=10.00,
    )

    assert trade.stop_loss == 5000.00


def test_trailing_stop_updates():
    """Trailing stop should advance."""

    trade = Trade(
        symbol="MES",
        direction="LONG",
        quantity=1,
        entry_price=5000.00,
        stop_loss=4990.00,
    )

    candle = {
        "high": 5022.00,
        "low": 5015.00,
        "close": 5020.00,
        "timestamp": datetime(2026, 8, 1, 10, 15),
    }

    ExitSimulator.process_candle(
        trade,
        candle,
        trail_distance=10.00,
    )

    assert trade.stop_loss == 5010.00


def test_partial_profit_reduces_quantity():
    """Partial profit should reduce position size."""

    trade = Trade(
        symbol="MES",
        direction="LONG",
        quantity=2,
        entry_price=5000.00,
        stop_loss=4990.00,
    )

    candle = {
        "high": 5015.00,
        "low": 5008.00,
        "close": 5012.00,
        "timestamp": datetime(2026, 8, 1, 10, 20),
    }

    ExitSimulator.process_candle(
        trade,
        candle,
        partial_target=5010.00,
        partial_quantity=1,
    )

    assert trade.quantity == 1
    assert trade.status == "OPEN"
