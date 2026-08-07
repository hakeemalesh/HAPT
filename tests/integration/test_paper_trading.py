"""
Tests for the HAPT Paper Trading Service.
"""

from app.execution.order import (
    Order,
    OrderSide,
    OrderType,
)
from app.execution.order_manager import OrderManager
from app.integration.paper_trading import (
    PaperTrade,
    PaperTradingService,
)


def make_managed_order(side=OrderSide.BUY, quantity=1):
    manager = OrderManager()

    order = Order(
        symbol="MES",
        side=side,
        order_type=OrderType.MARKET,
        quantity=quantity,
    )

    return manager.submit(order)


def test_initial_cash():
    service = PaperTradingService()

    assert service.cash == 100000.0
    assert service.starting_cash == 100000.0


def test_buy_execution():
    service = PaperTradingService()

    managed = make_managed_order()

    trade = service.execute(
        managed,
        execution_price=100.0,
    )

    assert isinstance(trade, PaperTrade)
    assert service.cash == 99900.0
    assert service.position("MES") == 1


def test_sell_execution():
    service = PaperTradingService()

    managed = make_managed_order(
        side=OrderSide.SELL,
    )

    service.execute(
        managed,
        execution_price=100.0,
    )

    assert service.cash == 100100.0
    assert service.position("MES") == -1


def test_trade_history():
    service = PaperTradingService()

    managed = make_managed_order()

    service.execute(
        managed,
        execution_price=100.0,
    )

    history = service.trade_history()

    assert len(history) == 1
    assert isinstance(history[0], PaperTrade)


def test_trade_count():
    service = PaperTradingService()

    service.execute(
        make_managed_order(),
        100.0,
    )

    service.execute(
        make_managed_order(),
        101.0,
    )

    assert service.total_trades() == 2


def test_timestamp_created():
    service = PaperTradingService()

    trade = service.execute(
        make_managed_order(),
        100.0,
    )

    assert trade.executed_at is not None
    assert trade.executed_at.tzinfo is not None


def test_custom_starting_cash():
    service = PaperTradingService(
        starting_cash=50000.0,
    )

    assert service.cash == 50000.0
    assert service.starting_cash == 50000.0
