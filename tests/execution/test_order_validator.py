"""
Tests for the HAPT Order Validation Engine.
"""

from app.execution.order import (
    Order,
    OrderSide,
    OrderType,
)
from app.execution.order_validator import (
    OrderValidator,
    ValidationResult,
)


def test_valid_market_order():
    order = Order(
        symbol="MES",
        side=OrderSide.BUY,
        order_type=OrderType.MARKET,
        quantity=1,
    )

    result = OrderValidator.validate(order)

    assert isinstance(result, ValidationResult)
    assert result.valid is True
    assert result.message == "Order is valid."


def test_valid_limit_order():
    order = Order(
        symbol="AAPL",
        side=OrderSide.SELL,
        order_type=OrderType.LIMIT,
        quantity=10,
        price=215.50,
    )

    result = OrderValidator.validate(order)

    assert result.valid is True


def test_valid_stop_order():
    order = Order(
        symbol="MNQ",
        side=OrderSide.BUY,
        order_type=OrderType.STOP,
        quantity=2,
        price=22850.0,
    )

    result = OrderValidator.validate(order)

    assert result.valid is True


def test_empty_symbol():
    order = Order(
        symbol="",
        side=OrderSide.BUY,
        order_type=OrderType.MARKET,
        quantity=1,
    )

    result = OrderValidator.validate(order)

    assert result.valid is False
    assert "Symbol" in result.message


def test_zero_quantity():
    order = Order(
        symbol="MES",
        side=OrderSide.BUY,
        order_type=OrderType.MARKET,
        quantity=0,
    )

    result = OrderValidator.validate(order)

    assert result.valid is False
    assert "Quantity" in result.message


def test_negative_quantity():
    order = Order(
        symbol="MES",
        side=OrderSide.BUY,
        order_type=OrderType.MARKET,
        quantity=-5,
    )

    result = OrderValidator.validate(order)

    assert result.valid is False


def test_limit_order_requires_price():
    order = Order(
        symbol="AAPL",
        side=OrderSide.BUY,
        order_type=OrderType.LIMIT,
        quantity=10,
        price=None,
    )

    result = OrderValidator.validate(order)

    assert result.valid is False
    assert "Price" in result.message


def test_stop_order_requires_price():
    order = Order(
        symbol="MNQ",
        side=OrderSide.SELL,
        order_type=OrderType.STOP,
        quantity=1,
        price=None,
    )

    result = OrderValidator.validate(order)

    assert result.valid is False


def test_limit_order_negative_price():
    order = Order(
        symbol="AAPL",
        side=OrderSide.BUY,
        order_type=OrderType.LIMIT,
        quantity=5,
        price=-100.0,
    )

    result = OrderValidator.validate(order)

    assert result.valid is False
