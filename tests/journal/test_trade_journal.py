"""
Tests for HAPT Trade Journal.
"""

from app.journal.trade_journal import TradeJournal
from app.models.trade import Trade


def create_trade(symbol="MES", grade="A", signal="BUY"):
    """Create a sample Trade object."""

    trade = Trade()

    trade.symbol = symbol
    trade.grade = grade
    trade.signal = signal
    trade.approved = True

    return trade


def test_new_journal_is_empty():
    """A new journal should contain no trades."""

    journal = TradeJournal()

    assert journal.count() == 0
    assert journal.get_trades() == []


def test_add_trade():
    """A trade should be recorded."""

    journal = TradeJournal()

    trade = create_trade()

    journal.add_trade(trade)

    assert journal.count() == 1
    assert journal.get_trades()[0] == trade


def test_add_multiple_trades():
    """Multiple trades should be stored."""

    journal = TradeJournal()

    journal.add_trade(create_trade("MES"))
    journal.add_trade(create_trade("MNQ"))
    journal.add_trade(create_trade("MGC"))

    assert journal.count() == 3

    trades = journal.get_trades()

    assert trades[0].symbol == "MES"
    assert trades[1].symbol == "MNQ"
    assert trades[2].symbol == "MGC"


def test_clear_journal():
    """Clearing removes every trade."""

    journal = TradeJournal()

    journal.add_trade(create_trade())

    journal.clear()

    assert journal.count() == 0
    assert journal.get_trades() == []


def test_get_trades_returns_copy():
    """
    The returned list should not expose
    the journal's internal storage.
    """

    journal = TradeJournal()

    journal.add_trade(create_trade())

    trades = journal.get_trades()

    trades.clear()

    assert journal.count() == 1


def test_trade_properties_preserved():
    """Stored Trade objects should keep their values."""

    journal = TradeJournal()

    trade = create_trade(
        symbol="MNQ",
        grade="A+",
        signal="BUY",
    )

    journal.add_trade(trade)

    stored = journal.get_trades()[0]

    assert stored.symbol == "MNQ"
    assert stored.grade == "A+"
    assert stored.signal == "BUY"