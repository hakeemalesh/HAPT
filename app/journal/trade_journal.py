"""
HAPT Trade Journal
------------------

Stores completed Trade objects for later analysis.
"""

from app.models.trade import Trade


class TradeJournal:
    """Stores completed HAPT trades."""

    def __init__(self):
        self._trades = []

    def add_trade(self, trade: Trade) -> None:
        """
        Add a completed trade.
        """

        if not isinstance(trade, Trade):
            raise TypeError(
                "trade must be a Trade instance."
            )

        self._trades.append(trade)

    def record_trade(self, trade: Trade) -> None:
        """
        Backwards-compatible alias for add_trade().
        """

        self.add_trade(trade)

    def get_trades(self) -> list[Trade]:
        """
        Return a copy of all recorded trades.
        """

        return list(self._trades)

    def get_latest_trade(self) -> Trade | None:
        """
        Return the most recently recorded trade.
        """

        if not self._trades:
            return None

        return self._trades[-1]

    def count(self) -> int:
        """
        Return the number of recorded trades.
        """

        return len(self._trades)

    def clear(self) -> None:
        """
        Remove all recorded trades.
        """

        self._trades.clear()