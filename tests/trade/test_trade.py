"""
Tests for the HAPT Trade Model.
"""

from datetime import datetime

from app.trade.trade import Trade


def test_trade_creation():
    """Trade should initialize correctly."""

    trade = Trade(
        symbol="MES",
        direction="LONG",
        quantity=2,
        entry_price=6125.25,
    )

    assert trade.symbol == "MES"
    assert trade.direction == "LONG"
    assert trade.quantity == 2
    assert trade.entry_price == 6125.25

    assert trade.status == "OPEN"

    assert trade.exit_price is None
    assert trade.exit_time is None
    assert trade.exit_reason is None

    assert trade.gross_pnl == 0.0
    assert trade.commission == 0.0
    assert trade.slippage == 0.0
    assert trade.net_pnl == 0.0


def test_trade_with_optional_fields():
    """Trade should store optional values."""

    now = datetime.now()

    trade = Trade(
        symbol="MNQ",
        direction="SHORT",
        quantity=1,
        entry_price=22550.75,
        entry_time=now,
        stop_loss=22600.00,
        take_profit=22450.00,
    )

    assert trade.entry_time == now
    assert trade.stop_loss == 22600.00
    assert trade.take_profit == 22450.00


def test_trade_closed():
    """Trade should support completed trades."""

    now = datetime.now()

    trade = Trade(
        symbol="ES",
        direction="LONG",
        quantity=1,
        entry_price=6200.00,
        exit_price=6210.50,
        exit_time=now,
        exit_reason="Take Profit",
        gross_pnl=525.00,
        commission=2.48,
        slippage=6.25,
        net_pnl=516.27,
        status="CLOSED",
    )

    assert trade.status == "CLOSED"
    assert trade.exit_price == 6210.50
    assert trade.exit_reason == "Take Profit"
    assert trade.net_pnl == 516.27
