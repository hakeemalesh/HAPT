"""
Tests for the HAPT Execution Engine.
"""

from app.execution.execution_engine import (
    ExecutionEngine,
    ExecutionResult,
)
from app.execution.order import (
    Order,
    OrderSide,
    OrderStatus,
    OrderType,
)
from app.execution.order_manager import OrderManager


def make_managed_order():
    manager = OrderManager()

    order = Order(
        symbol="MES",
        side=OrderSide.BUY,
        order_type=OrderType.MARKET,
        quantity=1,
    )

    return manager.submit(order)


def test_execute_market_order():
    managed = make_managed_order()

    result = ExecutionEngine.execute(
        managed,
        execution_price=6250.25,
    )

    assert isinstance(result, ExecutionResult)
    assert result.executed is True


def test_order_status_changes_to_filled():
    managed = make_managed_order()

    ExecutionEngine.execute(
        managed,
        execution_price=6250.25,
    )

    assert managed.order.status == OrderStatus.FILLED


def test_execution_price():
    managed = make_managed_order()

    result = ExecutionEngine.execute(
        managed,
        execution_price=500.50,
    )

    assert result.execution_price == 500.50


def test_execution_timestamp():
    managed = make_managed_order()

    result = ExecutionEngine.execute(
        managed,
        execution_price=100.0,
    )

    assert result.executed_at is not None
    assert result.executed_at.tzinfo is not None


def test_execution_order_id():
    managed = make_managed_order()

    result = ExecutionEngine.execute(
        managed,
        execution_price=100.0,
    )

    assert result.order_id == managed.order_id


def test_multiple_order_execution():
    manager = OrderManager()

    first = manager.submit(
        Order(
            symbol="MES",
            side=OrderSide.BUY,
            order_type=OrderType.MARKET,
            quantity=1,
        )
    )

    second = manager.submit(
        Order(
            symbol="MNQ",
            side=OrderSide.SELL,
            order_type=OrderType.MARKET,
            quantity=2,
        )
    )

    ExecutionEngine.execute(first, 6200.0)
    ExecutionEngine.execute(second, 22800.0)

    assert first.order.status == OrderStatus.FILLED
    assert second.order.status == OrderStatus.FILLED
