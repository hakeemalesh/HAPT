"""
Tests for the HAPT Replay Runner.
"""

from app.models.trade import Trade
from app.replay.replay_runner import ReplayRunner


class DummyReplayController:
    """Simple replay controller used for testing."""

    def __init__(self, contexts):
        self._contexts = list(contexts)
        self._index = 0
        self.symbol = None

    def load(
        self,
        symbol,
        candles,
    ):
        self.symbol = symbol
        self._index = 0

    def has_next(self):
        return self._index < len(self._contexts)

    def next_context(self):
        if not self.has_next():
            return None

        context = self._contexts[self._index]
        self._index += 1

        return context


class DummyStrategyEngine:
    """Simple strategy engine used for testing."""

    def analyze(
        self,
        context,
        entry_price,
    ):
        trade = Trade()

        trade.symbol = context["symbol"]
        trade.entry_price = entry_price
        trade.signal = "BUY"
        trade.approved = True

        return trade


def sample_contexts():
    """Return replay contexts."""

    return [
        {
            "symbol": "MES",
            "price": 100.0,
        },
        {
            "symbol": "MES",
            "price": 101.0,
        },
        {
            "symbol": "MES",
            "price": 102.0,
        },
    ]


def test_runner_returns_trade_journal():
    """ReplayRunner returns a populated journal."""

    runner = ReplayRunner(
        replay_controller=DummyReplayController(
            sample_contexts()
        ),
        strategy_engine=DummyStrategyEngine(),
    )

    journal = runner.run(
        "MES",
        [],
    )

    assert journal.count() == 3


def test_trade_symbol():
    """Trade symbol is preserved."""

    runner = ReplayRunner(
        replay_controller=DummyReplayController(
            sample_contexts()
        ),
        strategy_engine=DummyStrategyEngine(),
    )

    journal = runner.run(
        "MES",
        [],
    )

    trade = journal.get_latest_trade()

    assert trade.symbol == "MES"


def test_trade_price():
    """Entry price comes from replay context."""

    runner = ReplayRunner(
        replay_controller=DummyReplayController(
            sample_contexts()
        ),
        strategy_engine=DummyStrategyEngine(),
    )

    trade = runner.run(
        "MES",
        [],
    ).get_latest_trade()

    assert trade.entry_price == 102.0


def test_empty_replay():
    """Empty replay produces empty journal."""

    runner = ReplayRunner(
        replay_controller=DummyReplayController([]),
        strategy_engine=DummyStrategyEngine(),
    )

    journal = runner.run(
        "MES",
        [],
    )

    assert journal.count() == 0


def test_runner_skips_none_context():
    """ReplayRunner skips None contexts."""

    contexts = [
        {
            "symbol": "MES",
            "price": 100.0,
        },
        None,
        {
            "symbol": "MES",
            "price": 102.0,
        },
    ]

    runner = ReplayRunner(
        replay_controller=DummyReplayController(
            contexts
        ),
        strategy_engine=DummyStrategyEngine(),
    )

    journal = runner.run(
        "MES",
        [],
    )

    assert journal.count() == 2
