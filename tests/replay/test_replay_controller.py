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
    ):
        return {
            "symbol": symbol,
            "price": price,
            "candles": candles,
        }


def sample_candles():
    """Return sample replay candles."""

    return [
        {"close": 100.0},
        {"close": 101.0},
        {"close": 102.0},
    ]


def test_load():
    """ReplayController loads candles."""

    controller = ReplayController(
        replay_engine=DummyReplayEngine(),
        context_builder=DummyContextBuilder(),
    )

    controller.load(
        "MES",
        sample_candles(),
    )

    assert controller.has_next() is True
    assert controller.symbol == "MES"


def test_next_context():
    """ReplayController builds a context."""

    controller = ReplayController(
        replay_engine=DummyReplayEngine(),
        context_builder=DummyContextBuilder(),
    )

    controller.load(
        "MES",
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

    controller.load(
        "MES",
        [],
    )

    assert controller.next_context() is None


def test_symbol_is_preserved():
    """ReplayController preserves the replay symbol."""

    controller = ReplayController(
        replay_engine=DummyReplayEngine(),
        context_builder=DummyContextBuilder(),
    )

    controller.load(
        "MNQ",
        sample_candles(),
    )

    context = controller.next_context()

    assert context["symbol"] == "MNQ"
