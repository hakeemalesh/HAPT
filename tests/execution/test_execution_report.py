"""
Tests for the HAPT Professional Execution Report.
"""

from app.execution.execution_report import ExecutionReport
from app.execution.order import (
    Order,
    OrderSide,
    OrderStatus,
    OrderType,
)
from app.execution.order_manager import OrderManager


def make_order(status=OrderStatus.PENDING):
    manager = OrderManager()

    managed = manager.submit(
        Order(
            symbol="MES",
            side=OrderSide.BUY,
            order_type=OrderType.MARKET,
            quantity=1,
            status=status,
        )
    )

    return managed


def test_empty_report():
    report = ExecutionReport([])

    assert report.total_orders == 0
    assert report.success_rate == 0.0


def test_total_orders():
    report = ExecutionReport([
        make_order(),
        make_order(),
        make_order(),
    ])

    assert report.total_orders == 3


def test_filled_orders():
    report = ExecutionReport([
        make_order(OrderStatus.FILLED),
        make_order(OrderStatus.PENDING),
    ])

    assert report.filled_orders == 1


def test_cancelled_orders():
    report = ExecutionReport([
        make_order(OrderStatus.CANCELLED),
        make_order(OrderStatus.PENDING),
    ])

    assert report.cancelled_orders == 1


def test_rejected_orders():
    report = ExecutionReport([
        make_order(OrderStatus.REJECTED),
        make_order(OrderStatus.PENDING),
    ])

    assert report.rejected_orders == 1


def test_pending_orders():
    report = ExecutionReport([
        make_order(OrderStatus.PENDING),
        make_order(OrderStatus.FILLED),
    ])

    assert report.pending_orders == 1


def test_success_rate():
    report = ExecutionReport([
        make_order(OrderStatus.FILLED),
        make_order(OrderStatus.FILLED),
        make_order(OrderStatus.PENDING),
        make_order(OrderStatus.CANCELLED),
    ])

    assert report.success_rate == 50.0


def test_timestamp_created():
    report = ExecutionReport([])

    assert report.generated_at is not None
    assert report.generated_at.tzinfo is not None
