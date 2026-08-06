"""
Tests for the HAPT Replay Controller.
"""

from app.replay.replay_controller import ReplayController


class DummyReplayEngine:
    """Simple replay engine for testing."""

    def __init__(self):
        self._candles = []
        self._index = 0

    def load(self, candles):
        self._candles = list(candles)
        self._index = 0

    def has_next(self):
        return self._index < len(self._candles)

    def next(self):
        if not self.has_next():
            return None

        candle = self._candles[self._index]
        self._index += 1

        return candle

    def window(self, size):
        end = self._index
        start = max(0, end - size)
        return self._candles[start:end]


class DummyContextBuilder:
    """Simple context builder for testing."""

    def build(
        self,
        symbol,
        price,
        candles,
        current_time=None,
    ):
        return {
            "symbol": symbol,
            "price": price,
            "candles": candles,
            "current_time": current_time,
        }


def sample_candles(symbol="MES"):
    """Return sample replay candles."""

    return [
        {
            "symbol": symbol,
            "timestamp": "T0",
            "close": 100.0,
        },
        {
            "symbol": symbol,
            "timestamp": "T1",
            "close": 101.0,
        },
        {
            "symbol": symbol,
            "timestamp": "T2",
            "close": 102.0,
        },
    ]


def test_load():
    """ReplayController loads candles."""

    controller = ReplayController(
        replay_engine=DummyReplayEngine(),
        context_builder=DummyContextBuilder(),
    )

    controller.load(
        sample_candles(),
    )

    assert controller.has_next() is True


def test_next_context():
    """ReplayController builds a context."""

    controller = ReplayController(
        replay_engine=DummyReplayEngine(),
        context_builder=DummyContextBuilder(),
    )

    controller.load(
        sample_candles(),
    )

    context = controller.next_context()

    assert context["symbol"] == "MES"
    assert context["price"] == 100.0
    assert len(context["candles"]) == 1


def test_next_context_returns_none():
    """Replay ends correctly."""

    controller = ReplayController(
        replay_engine=DummyReplayEngine(),
        context_builder=DummyContextBuilder(),
    )

    controller.load([])

    assert controller.next_context() is None


def test_symbol_is_preserved():
    """ReplayController preserves the candle symbol."""

    controller = ReplayController(
        replay_engine=DummyReplayEngine(),
        context_builder=DummyContextBuilder(),
    )

    controller.load(
        sample_candles("MNQ"),
    )

    context = controller.next_context()

    assert context["symbol"] == "MNQ"