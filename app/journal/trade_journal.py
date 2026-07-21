"""
HAPT Trade Journal
------------------

Records trading decisions and trade history.
"""


class TradeJournal:
    """Stores completed trades."""

    def __init__(self):
        self.trades = []

    def record_trade(self, trade):
        """Save a completed trade."""

        self.trades.append(trade)

        print(f"Trade recorded: {trade['symbol']}")

    def get_trades(self):
        """Return all recorded trades."""

        return self.trades