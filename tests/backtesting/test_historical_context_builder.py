"""
Tests for the HAPT Historical Context Builder.
"""

from app.backtesting.historical_context_builder import (
    HistoricalContextBuilder,
)


class DummyPipeline:
    """Simple pipeline used for testing."""

    def __init__(self, result):
        self.result = result

    def build_context(
        self,
        symbol,
        price,
    ):
        return self.result


def test_builder_instantiates():
    """Builder can be created."""

    builder = HistoricalContextBuilder()

    assert builder is not None


def test_build_returns_pipeline_result():
    """Builder returns pipeline output."""

    expected = {
        "symbol": "MES",
        "price": 7772.0,
    }

    builder = HistoricalContextBuilder()
    builder.pipeline = DummyPipeline(expected)

    result = builder.build(
        "MES",
        7772.0,
    )

    assert result == expected


def test_build_returns_none():
    """Builder propagates None."""

    builder = HistoricalContextBuilder()
    builder.pipeline = DummyPipeline(None)

    result = builder.build(
        "MES",
        7772.0,
    )

    assert result is None
