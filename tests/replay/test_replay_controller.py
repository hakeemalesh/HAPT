"""
Tests for the HAPT Replay Controller.
"""

from app.replay.replay_controller import ReplayController


class DummyReplayEngine:
    """Simple replay engine used for testing."""

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
        if size <= 0:
            return []

        end = self._index
        start = max(0, end - size)

        return self._candles[start:end]


class DummyContextBuilder:
    """Simple context builder used for testing."""

    def build(
        self,
        symbol,
        price,
        candles=None,
    ):
        return {
            "symbol": symbol,
            "price": price,
            "window_size": len(candles or []),
            "built": True,
        }


def sample_candles():
    """Return sample replay candles."""

    return [
        {
            "symbol": "MES",
            "close": 100,
        },
        {
            "symbol": "MES",
            "close": 101,
        },
        {
            "symbol": "MES",
            "close": 102,
        },
    ]


def test_load():
    """ReplayController loads candles."""

    controller = ReplayController(
        replay_engine=DummyReplayEngine(),
        context_builder=DummyContextBuilder(),
    )

    controller.load(sample_candles())

    assert controller.has_next() is True


def test_next_context():
    """ReplayController builds production context."""

    controller = ReplayController(
        replay_engine=DummyReplayEngine(),
        context_builder=DummyContextBuilder(),
    )

    controller.load(sample_candles())

    context = controller.next_context()

    assert context["symbol"] == "MES"
    assert context["price"] == 100
    assert context["window_size"] == 1
    assert context["built"] is True


def test_window_grows():
    """Replay window grows as replay advances."""

    controller = ReplayController(
        replay_engine=DummyReplayEngine(),
        context_builder=DummyContextBuilder(),
    )

    controller.load(sample_candles())

    controller.next_context()

    context = controller.next_context()

    assert context["window_size"] == 2


def test_next_context_returns_none():
    """Replay ends correctly."""

    controller = ReplayController(
        replay_engine=DummyReplayEngine(),
        context_builder=DummyContextBuilder(),
    )

    controller.load([])

    assert controller.next_context() is None
