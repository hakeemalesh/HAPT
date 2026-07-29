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
        """Add a completed trade."""

        self._trades.append(trade)

    def record_trade(self, trade: Trade) -> None:
        """
        Backwards-compatible alias for add_trade().
        """

        self.add_trade(trade)

    def get_trades(self) -> list[Trade]:
        """Return all recorded trades."""

        return list(self._trades)

    def count(self) -> int:
        """Return the number of recorded trades."""

        return len(self._trades)

    def clear(self) -> None:
        """Remove all recorded trades."""

        self._trades.clear()