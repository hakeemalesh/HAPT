"""
Tests for the HAPT Backtesting Engine.
"""

from app.backtesting.backtest_engine import BacktestEngine
from app.journal.trade_journal import TradeJournal
from app.models.trade import Trade


class DummyStrategyEngine:
    """Simple strategy engine for testing."""

    def __init__(self, results):
        self._results = results
        self._index = 0

    def evaluate(self, candle):
        """Return the next predefined result."""

        if self._index >= len(self._results):
            return None

        result = self._results[self._index]
        self._index += 1
        return result


def create_trade():
    """Create a sample trade."""

    trade = Trade()
    trade.signal = "BUY"
    trade.grade = "A"
    trade.approved = True
    trade.risk_reward = 2.0
    return trade


def test_empty_backtest():
    """Empty candles should produce an empty journal."""

    strategy = DummyStrategyEngine([])

    engine = BacktestEngine(strategy)

    journal = engine.run([])

    assert isinstance(journal, TradeJournal)
    assert journal.count() == 0


def test_single_trade_added():
    """One trade should be added."""

    trade = create_trade()

    strategy = DummyStrategyEngine([trade])

    engine = BacktestEngine(strategy)

    journal = engine.run([{"close": 100}])

    assert journal.count() == 1
    assert journal.get_trades()[0] is trade


def test_multiple_trades_added():
    """Multiple trades should all be recorded."""

    trades = [
        create_trade(),
        create_trade(),
        create_trade(),
    ]

    strategy = DummyStrategyEngine(trades)

    engine = BacktestEngine(strategy)

    candles = [
        {"close": 100},
        {"close": 101},
        {"close": 102},
    ]

    journal = engine.run(candles)

    assert journal.count() == 3


def test_none_results_not_added():
    """None values should not be recorded."""

    strategy = DummyStrategyEngine([
        create_trade(),
        None,
        create_trade(),
    ])

    engine = BacktestEngine(strategy)

    candles = [
        {"close": 100},
        {"close": 101},
        {"close": 102},
    ]

    journal = engine.run(candles)

    assert journal.count() == 2


def test_returns_trade_journal():
    """Run should always return a TradeJournal."""

    strategy = DummyStrategyEngine([])

    engine = BacktestEngine(strategy)

    journal = engine.run([])

    assert isinstance(journal, TradeJournal)