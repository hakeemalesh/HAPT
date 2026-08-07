"""
Tests for the HAPT Trade Lifecycle Manager.
"""

from app.execution.order import (
    Order,
    OrderSide,
    OrderStatus,
    OrderType,
)
from app.execution.order_manager import OrderManager
from app.execution.trade_lifecycle import (
    LifecycleEvent,
    TradeLifecycle,
)


def make_lifecycle():
    manager = OrderManager()

    managed = manager.submit(
        Order(
            symbol="MES",
            side=OrderSide.BUY,
            order_type=OrderType.MARKET,
            quantity=1,
        )
    )

    return TradeLifecycle(managed)


def test_initial_event():
    lifecycle = make_lifecycle()

    history = lifecycle.history()

    assert len(history) == 1
    assert isinstance(history[0], LifecycleEvent)
    assert history[0].status == OrderStatus.PENDING


def test_valid_transition():
    lifecycle = make_lifecycle()

    assert lifecycle.transition_to(
        OrderStatus.VALIDATED
    ) is True

    assert (
        lifecycle.current_status()
        == OrderStatus.VALIDATED
    )


def test_invalid_transition():
    lifecycle = make_lifecycle()

    assert lifecycle.transition_to(
        OrderStatus.FILLED
    ) is False

    assert (
        lifecycle.current_status()
        == OrderStatus.PENDING
    )


def test_multiple_valid_transitions():
    lifecycle = make_lifecycle()

    assert lifecycle.transition_to(
        OrderStatus.VALIDATED
    )

    assert lifecycle.transition_to(
        OrderStatus.SUBMITTED
    )

    assert lifecycle.transition_to(
        OrderStatus.FILLED
    )

    assert (
        lifecycle.current_status()
        == OrderStatus.FILLED
    )


def test_history_records_events():
    lifecycle = make_lifecycle()

    lifecycle.transition_to(
        OrderStatus.VALIDATED
    )

    lifecycle.transition_to(
        OrderStatus.SUBMITTED
    )

    history = lifecycle.history()

    assert len(history) == 3

    assert history[1].status == OrderStatus.VALIDATED
    assert history[2].status == OrderStatus.SUBMITTED


def test_event_count():
    lifecycle = make_lifecycle()

    lifecycle.transition_to(
        OrderStatus.VALIDATED
    )

    assert lifecycle.event_count() == 2


def test_event_timestamps():
    lifecycle = make_lifecycle()

    event = lifecycle.history()[0]

    assert event.timestamp is not None
    assert event.timestamp.tzinfo is not None
