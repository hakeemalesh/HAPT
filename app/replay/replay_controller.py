"""
HAPT Replay Controller
----------------------

Coordinates historical replay by combining the
ReplayEngine and HistoricalContextBuilder.
"""

from app.backtesting.historical_context_builder import (
    HistoricalContextBuilder,
)
from app.replay.replay_engine import ReplayEngine


class ReplayController:
    """
    Coordinates historical replay.
    """

    def __init__(
        self,
        replay_engine=None,
        context_builder=None,
    ):
        """Initialize replay controller."""

        self.replay_engine = (
            replay_engine
            if replay_engine is not None
            else ReplayEngine()
        )

        self.context_builder = (
            context_builder
            if context_builder is not None
            else HistoricalContextBuilder()
        )

    def load(
        self,
        candles,
    ):
        """
        Load historical candles.
        """

        self.replay_engine.load(candles)

    def has_next(self):
        """
        Return True if replay can continue.
        """

        return self.replay_engine.has_next()

    def next_context(self):
        """
        Advance replay and build context.

        Returns
        -------
        dict | None
            Historical market context, or None
            when replay has finished.
        """

        candle = self.replay_engine.next()

        if candle is None:
            return None

        return self.context_builder.build(candle)
