"""
HAPT Account Manager
--------------------

Manages trading account information and
calculates allowable trade risk.
"""


class AccountManager:
    """Manages account settings."""

    DEFAULT_BALANCE = 3000.00
    DEFAULT_RISK_PERCENT = 1.0

    def __init__(
        self,
        balance=DEFAULT_BALANCE,
        risk_percent=DEFAULT_RISK_PERCENT,
    ):
        """Initialize account settings."""

        self.balance = balance
        self.risk_percent = risk_percent

    def get_balance(self):
        """Return account balance."""

        return self.balance

    def get_risk_percent(self):
        """Return risk percentage."""

        return self.risk_percent

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