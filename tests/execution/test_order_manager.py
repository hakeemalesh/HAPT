"""
Tests for the HAPT Order Management System.
"""

from app.execution.order import (
    Order,
    OrderSide,
    OrderStatus,
    OrderType,
)
from app.execution.order_manager import (
    ManagedOrder,
    OrderManager,
)


def make_order():
    return Order(
        symbol="MES",
        side=OrderSide.BUY,
        order_type=OrderType.MARKET,
        quantity=1,
    )


def test_submit_order():
    manager = OrderManager()

    managed = manager.submit(make_order())

    assert isinstance(managed, ManagedOrder)
    assert managed.order_id == 1
    assert managed.order.symbol == "MES"


def test_order_ids_increment():
    manager = OrderManager()

    first = manager.submit(make_order())
    second = manager.submit(make_order())

    assert second.order_id == first.order_id + 1


def test_get_order():
    manager = OrderManager()

    managed = manager.submit(make_order())

    retrieved = manager.get(managed.order_id)

    assert retrieved is managed


def test_update_status():
    manager = OrderManager()

    managed = manager.submit(make_order())

    updated = manager.update_status(
        managed.order_id,
        OrderStatus.VALIDATED,
    )

    assert updated is True
    assert (
        managed.order.status
        == OrderStatus.VALIDATED
    )


def test_cancel_order():
    manager = OrderManager()

    managed = manager.submit(make_order())

    cancelled = manager.cancel(
        managed.order_id,
    )

    assert cancelled is True
    assert (
        managed.order.status
        == OrderStatus.CANCELLED
    )


def test_active_orders():
    manager = OrderManager()

    active = manager.submit(make_order())

    cancelled = manager.submit(make_order())

    manager.cancel(cancelled.order_id)

    active_orders = manager.active_orders()

    assert len(active_orders) == 1
    assert (
        active_orders[0].order_id
        == active.order_id
    )


def test_total_orders():
    manager = OrderManager()

    manager.submit(make_order())
    manager.submit(make_order())
    manager.submit(make_order())

    assert manager.total_orders() == 3


def test_missing_order_returns_none():
    manager = OrderManager()

    assert manager.get(9999) is None


def test_update_missing_order():
    manager = OrderManager()

    updated = manager.update_status(
        9999,
        OrderStatus.FILLED,
    )

    assert updated is False
