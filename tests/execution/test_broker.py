"""
Tests for the HAPT Broker Abstraction Layer.
"""

from app.execution.broker import (
    Broker,
    PaperBroker,
)
from app.execution.order import (
    Order,
    OrderSide,
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


def test_paper_broker_is_broker():
    broker = PaperBroker()

    assert isinstance(broker, Broker)


def test_connect():
    broker = PaperBroker()

    assert broker.connect() is True
    assert broker.connected is True


def test_disconnect():
    broker = PaperBroker()

    broker.connect()

    assert broker.disconnect() is True
    assert broker.connected is False


def test_submit_order_connected():
    broker = PaperBroker()

    broker.connect()

    managed = make_managed_order()

    assert broker.submit_order(managed) is True


def test_submit_order_disconnected():
    broker = PaperBroker()

    managed = make_managed_order()

    assert broker.submit_order(managed) is False


def test_cancel_order():
    broker = PaperBroker()

    broker.connect()

    managed = make_managed_order()

    broker.submit_order(managed)

    assert broker.cancel_order(managed.order_id) is True


def test_account_balance():
    broker = PaperBroker()

    assert broker.account_balance() == 100000.0


def test_positions():
    broker = PaperBroker()

    broker.connect()

    managed = make_managed_order()

    broker.submit_order(managed)

    positions = broker.positions()

    assert positions == ["MES"]
