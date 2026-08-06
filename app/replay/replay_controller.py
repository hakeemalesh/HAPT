"""
HAPT Replay Controller
----------------------

Coordinates historical replay using the production
ReplayEngine and HistoricalContextBuilder.
"""

from datetime import datetime

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

    def _parse_timestamp(
        self,
        candle,
    ):
        """
        Convert a candle timestamp into a datetime.

        Returns None if the timestamp cannot be
        interpreted (for example demo data like "T17").
        """

        timestamp = candle.get("timestamp")

        if isinstance(timestamp, datetime):
            return timestamp

        if not isinstance(timestamp, str):
            return None

        #
        # Demo timestamps ("T17") are intentionally ignored.
        #
        if timestamp.startswith("T"):
            return None

        try:
            #
            # Yahoo timestamps are stored as strings.
            #
            return datetime.fromisoformat(
                timestamp.replace("Z", "+00:00")
            )

        except ValueError:
            return None

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
            symbol=candle.get("symbol", "UNKNOWN"),
            price=candle["close"],
            candles=window,
            current_time=self._parse_timestamp(
                candle
            ),
        )
