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


class DummyContextBuilder:
    """Simple context builder for testing."""

    def build(self, candle):
        return {
            "close": candle["close"],
            "built": True,
        }


def sample_candles():
    """Return sample candles."""

    return [
        {"close": 100},
        {"close": 101},
        {"close": 102},
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
    """ReplayController builds context."""

    controller = ReplayController(
        replay_engine=DummyReplayEngine(),
        context_builder=DummyContextBuilder(),
    )

    controller.load(sample_candles())

    context = controller.next_context()

    assert context["close"] == 100
    assert context["built"] is True


def test_next_context_returns_none():
    """Replay ends correctly."""

    controller = ReplayController(
        replay_engine=DummyReplayEngine(),
        context_builder=DummyContextBuilder(),
    )

    controller.load([])

    assert controller.next_context() is None
