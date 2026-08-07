"""
End-to-end integration tests for the HAPT trading pipeline.
"""

from app.execution.order import (
    Order,
    OrderSide,
    OrderType,
)
from app.execution.order_manager import OrderManager
from app.integration.broker_config import BrokerConfig
from app.integration.credentials_manager import Credentials
from app.integration.execution_monitor import ExecutionMonitor
from app.integration.interactive_brokers import (
    InteractiveBrokersAdapter,
    MockIBClient,
)
from app.integration.paper_trading import PaperTradingService


def valid_credentials():
    return Credentials(
        username="user",
        password="pass",
        api_key="key",
        api_secret="secret",
    )


def create_managed_order():
    manager = OrderManager()

    order = Order(
        symbol="MES",
        side=OrderSide.BUY,
        order_type=OrderType.MARKET,
        quantity=2,
    )

    return manager.submit(order)


def test_complete_paper_trading_workflow():
    service = PaperTradingService()

    managed = create_managed_order()

    trade = service.execute(
        managed,
        execution_price=100.0,
    )

    assert trade.order.order.symbol == "MES"
    assert service.position("MES") == 2
    assert service.cash == 99800.0
    assert service.total_trades() == 1


def test_broker_connection_workflow():
    adapter = InteractiveBrokersAdapter(
        config=BrokerConfig(),
        credentials=valid_credentials(),
        client=MockIBClient(),
    )

    assert adapter.connect() is True
    assert adapter.connected is True

    assert adapter.disconnect() is True
    assert adapter.connected is False


def test_execution_monitor_workflow():
    monitor = ExecutionMonitor()

    monitor.connect()

    monitor.record_submission()
    monitor.record_fill()

    assert monitor.connected is True
    assert monitor.success_rate == 100.0
    assert monitor.health == "HEALTHY"


def test_multiple_trade_session():
    service = PaperTradingService()

    service.execute(
        create_managed_order(),
        100.0,
    )

    service.execute(
        create_managed_order(),
        105.0,
    )

    assert service.total_trades() == 2
    assert service.position("MES") == 4


def test_monitor_with_rejection():
    monitor = ExecutionMonitor()

    monitor.connect()
    monitor.record_submission()
    monitor.record_rejection()

    assert monitor.health == "WARNING"


def test_broker_and_monitor_together():
    adapter = InteractiveBrokersAdapter(
        config=BrokerConfig(),
        credentials=valid_credentials(),
        client=MockIBClient(),
    )

    monitor = ExecutionMonitor()

    assert adapter.connect() is True

    monitor.connect()
    monitor.record_submission()
    monitor.record_fill()

    assert adapter.connected is True
    assert monitor.success_rate == 100.0


def test_trade_history_consistency():
    service = PaperTradingService()

    service.execute(
        create_managed_order(),
        101.25,
    )

    history = service.trade_history()

    assert len(history) == service.total_trades()
    assert history[0].execution_price == 101.25


def test_cash_and_positions_consistency():
    service = PaperTradingService()

    service.execute(
        create_managed_order(),
        100.0,
    )

    assert service.cash < service.starting_cash
    assert service.position("MES") > 0
