"""
Manages trading account information and
maintains the live account state.
"""

from app.account_state.account_state import AccountState
from app.config.trading_account import (
    ACCOUNT_BALANCE,
    ACCOUNT_CURRENCY,
    ACCOUNT_NAME,
    RISK_PERCENT,
)


class AccountManager:
    """Manages account settings and live account state."""

    def __init__(
        self,
        balance: float = ACCOUNT_BALANCE,
        risk_percent: float = RISK_PERCENT,
        currency: str = ACCOUNT_CURRENCY,
        account_name: str = ACCOUNT_NAME,
    ) -> None:
        """Initialize account settings."""

        self.balance: float = balance
        self.risk_percent: float = risk_percent
        self.currency: str = currency
        self.account_name: str = account_name

        self.state: AccountState = AccountState(
            starting_balance=balance,
            current_balance=balance,
            buying_power=balance,
            available_margin=balance,
        )

    def get_balance(self) -> float:
        """Return account balance."""

        return self.state.current_balance

    def get_buying_power(self) -> float:
        """
        Return available buying power.
        """

        return self.state.buying_power

    def get_risk_percent(self) -> float:
        """Return risk percentage."""

        return self.risk_percent

    def get_currency(self) -> str:
        """Return account currency."""

        return self.currency

    def get_account_name(self) -> str:
        """Return account name."""

        return self.account_name

    def get_max_trade_risk(self) -> float:
        """
        Return maximum allowable dollar
        risk for one trade.
        """

        return round(
            self.get_balance()
            * (self.risk_percent / 100),
            2,
        )

    def get_state(self) -> AccountState:
        """Return the live account state."""

        return self.state

    def update_balance(
        self,
        new_balance: float,
    ) -> None:
        """Update account balance."""

        self.state.update_balance(new_balance)

    def update_risk_percent(
        self,
        risk_percent: float,
    ) -> None:
        """Update risk percentage."""

        self.risk_percent = risk_percent

    def update_currency(
        self,
        currency: str,
    ) -> None:
        """Update account currency."""

        self.currency = currency

    def update_account_name(
        self,
        account_name: str,
    ) -> None:
        """Update account name."""

        self.account_name = account_name