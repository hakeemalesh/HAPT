"""
Tests for the HAPT Replay Engine.
"""

from app.replay.replay_engine import ReplayEngine


def sample_candles():
    """Return sample candles."""

    return [
        {"close": 100},
        {"close": 101},
        {"close": 102},
    ]


def test_engine_instantiates():
    """ReplayEngine can be created."""

    engine = ReplayEngine()

    assert engine is not None


def test_load_candles():
    """Engine loads candles."""

    engine = ReplayEngine()

    engine.load(sample_candles())

    assert engine.progress() == (0, 3)


def test_has_next():
    """Engine reports remaining candles."""

    engine = ReplayEngine()

    engine.load(sample_candles())

    assert engine.has_next() is True


def test_next_returns_first_candle():
    """First candle is returned."""

    engine = ReplayEngine()

    engine.load(sample_candles())

    candle = engine.next()

    assert candle["close"] == 100


def test_current_returns_last_candle():
    """Current returns latest replayed candle."""

    engine = ReplayEngine()

    engine.load(sample_candles())

    engine.next()

    assert engine.current()["close"] == 100


def test_reset():
    """Reset restarts replay."""

    engine = ReplayEngine()

    engine.load(sample_candles())

    engine.next()

    engine.reset()

    assert engine.progress() == (0, 3)


def test_next_returns_none_when_finished():
    """Replay ends correctly."""

    engine = ReplayEngine()

    engine.load(sample_candles())

    engine.next()
    engine.next()
    engine.next()

    assert engine.next() is None
