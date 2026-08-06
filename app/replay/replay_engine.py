"""
HAPT Replay Engine
------------------

Replays historical market data one candle at a time.

The ReplayEngine is responsible only for managing the
historical candle stream. It does not calculate
indicators, make trading decisions, or execute trades.
"""


class ReplayEngine:
    """
    Provides sequential access to historical candles.
    """

    def __init__(self):
        """Initialize the replay engine."""

        self._candles = []
        self._index = 0

    def load(
        self,
        candles,
    ):
        """
        Load historical candles.
        """

        self._candles = list(candles)
        self._index = 0

    def reset(self):
        """
        Restart replay from the beginning.
        """

        self._index = 0

    def has_next(self):
        """
        Return True if another candle exists.
        """

        return self._index < len(self._candles)

    def next(self):
        """
        Return the next candle.
        """

        if not self.has_next():
            return None

        candle = self._candles[self._index]
        self._index += 1

        return candle

    def current(self):
        """
        Return the current candle.
        """

        if self._index == 0:
            return None

        return self._candles[self._index - 1]

    def progress(self):
        """
        Return replay progress.
        """

        return (
            self._index,
            len(self._candles),
        )
