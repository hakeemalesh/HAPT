"""
HAPT Replay Controller
----------------------

Coordinates historical replay using the production
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

    DEFAULT_WINDOW_SIZE = 200

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

        #
        # Symbol currently being replayed.
        #
        self.symbol = None

    def load(
        self,
        symbol,
        candles,
    ):
        """
        Load historical candles for a symbol.
        """

        self.symbol = symbol

        self.replay_engine.load(candles)

    def has_next(self):
        """
        Return True if replay can continue.
        """

        return self.replay_engine.has_next()

    def next_context(self):
        """
        Advance replay by one candle and build a
        production market context.

        Returns
        -------
        dict | None
        """

        candle = self.replay_engine.next()

        if candle is None:
            return None

        window = self.replay_engine.window(
            self.DEFAULT_WINDOW_SIZE
        )

        return self.context_builder.build(
            symbol=self.symbol,
            price=candle["close"],
            candles=window,
        )
