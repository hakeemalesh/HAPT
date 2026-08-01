"""
HAPT Account State
------------------

Tracks the live state of the trading account
during a trading session.
"""

from dataclasses import dataclass


@dataclass
class AccountState:
    """
    Represents the live trading account state.
    """

    starting_balance: float = 0.0

    current_balance: float = 0.0

    daily_profit: float = 0.0

    daily_loss: float = 0.0

    buying_power: float = 0.0

    available_margin: float = 0.0

    open_trades: int = 0

    winning_trades: int = 0

    losing_trades: int = 0

    drawdown: float = 0.0

    trading_enabled: bool = True

    def update_balance(
        self,
        new_balance: float,
    ):
        """
        Update the current account balance.
        """

        self.current_balance = new_balance

        pnl = (
            self.current_balance
            - self.starting_balance
        )

        if pnl >= 0:

            self.daily_profit = pnl
            self.daily_loss = 0.0

        else:

            self.daily_profit = 0.0
            self.daily_loss = abs(pnl)

    def record_win(self):
        """
        Record a winning trade.
        """

        self.winning_trades += 1

    def record_loss(self):
        """
        Record a losing trade.
        """

        self.losing_trades += 1

    def increment_open_trades(self):
        """
        Increase the number of open trades.
        """

        self.open_trades += 1

    def decrement_open_trades(self):
        """
        Decrease the number of open trades.
        """

        if self.open_trades > 0:
            self.open_trades -= 1