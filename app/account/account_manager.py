"""
HAPT Account Manager
--------------------

Manages trading account information and
maintains the live account state.
"""

from app.account_state.account_state import AccountState
from app.config.trading_account import (
    ACCOUNT_BALANCE,
    RISK_PERCENT,
    ACCOUNT_CURRENCY,
    ACCOUNT_NAME,
)


class AccountManager:
    """Manages account settings and live account state."""

    def __init__(
        self,
        balance=ACCOUNT_BALANCE,
        risk_percent=RISK_PERCENT,
        currency=ACCOUNT_CURRENCY,
        account_name=ACCOUNT_NAME,
    ):
        """Initialize account settings."""

        self.balance = balance
        self.risk_percent = risk_percent
        self.currency = currency
        self.account_name = account_name

        self.state = AccountState(
            starting_balance=balance,
            current_balance=balance,
            buying_power=balance,
            available_margin=balance,
        )

    def get_balance(self):
        """Return account balance."""

        return self.state.current_balance

    def get_buying_power(self):
        """
        Return available buying power.
        """

        return self.state.buying_power

    def get_risk_percent(self):
        """Return risk percentage."""

        return self.risk_percent

    def get_currency(self):
        """Return account currency."""

        return self.currency

    def get_account_name(self):
        """Return account name."""

        return self.account_name

    def get_max_trade_risk(self):
        """
        Return maximum allowable dollar
        risk for one trade.
        """

        return round(
            self.get_balance()
            * (self.risk_percent / 100),
            2,
        )

    def get_state(self):
        """Return the live account state."""

        return self.state

    def update_balance(
        self,
        new_balance,
    ):
        """Update account balance."""

        self.state.update_balance(new_balance)

    def update_risk_percent(
        self,
        risk_percent,
    ):
        """Update risk percentage."""

        self.risk_percent = risk_percent

    def update_currency(
        self,
        currency,
    ):
        """Update account currency."""

        self.currency = currency

    def update_account_name(
        self,
        account_name,
    ):
        """Update account name."""

        self.account_name = account_name