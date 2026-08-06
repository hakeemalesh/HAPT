"""
HAPT Trade Journal
------------------

Stores completed Trade objects for later analysis.
"""

from app.models.trade import Trade


class TradeJournal:
    """Stores completed HAPT trades."""

    def __init__(self):
        """Initialize the trade journal."""

        self._trades = []

    def add_trade(
        self,
        trade: Trade,
    ) -> None:
        """
        Add a completed trade.
        """

        if not isinstance(trade, Trade):

            raise TypeError(
                "trade must be a Trade instance."
            )

        self._trades.append(trade)

    def record_trade(
        self,
        trade: Trade,
    ) -> None:
        """
        Backwards-compatible alias.
        """

        self.add_trade(trade)

    def get_trades(self) -> list[Trade]:
        """
        Return all recorded trades.
        """

        return list(self._trades)

    def get_latest_trade(
        self,
    ) -> Trade | None:
        """
        Return the most recent trade.
        """

        if not self._trades:
            return None

        return self._trades[-1]

    def approved_trades(self) -> list[Trade]:
        """
        Return approved trades.
        """

        return [
            trade
            for trade in self._trades
            if trade.approved
        ]

    def rejected_trades(self) -> list[Trade]:
        """
        Return rejected trades.
        """

        return [
            trade
            for trade in self._trades
            if not trade.approved
        ]

    def count(self) -> int:
        """
        Return number of recorded trades.
        """

        return len(self._trades)

    def approved_count(self) -> int:
        """
        Return number of approved trades.
        """

        return len(
            self.approved_trades()
        )

    def rejected_count(self) -> int:
        """
        Return number of rejected trades.
        """

        return len(
            self.rejected_trades()
        )

    def approval_rate(self) -> float:
        """
        Return approval percentage.
        """

        total = self.count()

        if total == 0:
            return 0.0

        return round(
            (
                self.approved_count()
                / total
            ) * 100,
            2,
        )

    def winning_trades(self) -> int:
        """
        Return the number of winning trades.
        """

        return sum(
            1
            for trade in self._trades
            if trade.profit_loss > 0
        )

    def losing_trades(self) -> int:
        """
        Return the number of losing trades.
        """

        return sum(
            1
            for trade in self._trades
            if trade.profit_loss < 0
        )

    def total_profit(self) -> float:
        """
        Return total realized profit.
        """

        return round(
            sum(
                trade.profit_loss
                for trade in self._trades
                if trade.profit_loss > 0
            ),
            2,
        )

    def total_loss(self) -> float:
        """
        Return total realized loss.
        """

        return round(
            sum(
                trade.profit_loss
                for trade in self._trades
                if trade.profit_loss < 0
            ),
            2,
        )

    def net_profit(self) -> float:
        """
        Return overall net profit.
        """

        return round(
            sum(
                trade.profit_loss
                for trade in self._trades
            ),
            2,
        )

    def clear(self) -> None:
        """
        Remove all recorded trades.
        """

        self._trades.clear()
