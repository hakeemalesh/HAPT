"""
Tests for the HAPT Order Model.
"""

from app.execution.order import (
    Order,
    OrderSide,
    OrderStatus,
    OrderType,
)


def test_market_order_creation():
    order = Order(
        symbol="MES",
        side=OrderSide.BUY,
        order_type=OrderType.MARKET,
        quantity=2,
    )

    assert order.symbol == "MES"
    assert order.side == OrderSide.BUY
    assert order.order_type == OrderType.MARKET
    assert order.quantity == 2
    assert order.price is None


def test_limit_order_creation():
    order = Order(
        symbol="AAPL",
        side=OrderSide.SELL,
        order_type=OrderType.LIMIT,
        quantity=10,
        price=215.50,
    )

    assert order.order_type == OrderType.LIMIT
    assert order.price == 215.50


def test_stop_order_creation():
    order = Order(
        symbol="MNQ",
        side=OrderSide.BUY,
        order_type=OrderType.STOP,
        quantity=1,
        price=22850.00,
    )

    assert order.order_type == OrderType.STOP
    assert order.price == 22850.00


def test_default_status():
    order = Order(
        symbol="MES",
        side=OrderSide.BUY,
        order_type=OrderType.MARKET,
        quantity=1,
    )

    assert order.status == OrderStatus.PENDING


def test_timestamp_created():
    order = Order(
        symbol="MES",
        side=OrderSide.BUY,
        order_type=OrderType.MARKET,
        quantity=1,
    )

    assert order.created_at is not None
    assert order.created_at.tzinfo is not None


def test_order_status_assignment():
    order = Order(
        symbol="MES",
        side=OrderSide.BUY,
        order_type=OrderType.MARKET,
        quantity=1,
        status=OrderStatus.VALIDATED,
    )

    assert order.status == OrderStatus.VALIDATED


def test_enum_values():
    assert OrderSide.BUY.value == "BUY"
    assert OrderSide.SELL.value == "SELL"

    assert OrderType.MARKET.value == "MARKET"
    assert OrderType.LIMIT.value == "LIMIT"
    assert OrderType.STOP.value == "STOP"

    assert OrderStatus.PENDING.value == "PENDING"
    assert OrderStatus.FILLED.value == "FILLED"
