"""
HAPT Account Manager
--------------------

Manages trading account information and
calculates allowable trade risk.
"""

from app.config.trading_account import (
    ACCOUNT_BALANCE,
    RISK_PERCENT,
    ACCOUNT_CURRENCY,
    ACCOUNT_NAME,
)


class AccountManager:
    """Manages account settings."""

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

    def get_balance(self):
        """Return account balance."""

        return self.balance

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
        Return maximum dollar risk
        allowed for one trade.
        """

        return round(
            self.balance
            * (self.risk_percent / 100),
            2,
        )

    def update_balance(
        self,
        balance,
    ):
        """Update account balance."""

        self.balance = balance

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