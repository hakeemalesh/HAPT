"""
HAPT Trade Validator
--------------------

Validates completed trade plans before
execution.
"""

from app.models.trade import Trade


class TradeValidator:
    """
    Validates completed trade plans.
    """

    MIN_RISK_REWARD = 1.5

    def validate(
        self,
        trade: Trade,
    ) -> bool:
        """
        Return True if a trade is
        executable.
        """

        if not trade.approved:
            return False

        if trade.signal not in (
            "BUY",
            "SELL",
        ):
            return False

        if trade.position_size <= 0:
            return False

        if trade.entry_price <= 0:
            return False

        if trade.stop_loss <= 0:
            return False

        if trade.target_price <= 0:
            return False

        if trade.risk_amount <= 0:
            return False

        if trade.risk_reward < self.MIN_RISK_REWARD:
            return False

        return True
