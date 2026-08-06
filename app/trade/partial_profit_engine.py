"""
HAPT Partial Profit Engine
--------------------------

Scales out of a position when a target
price has been reached.
"""

from app.trade.trade import Trade


class PartialProfitEngine:
    """Handles partial profit taking."""

    @staticmethod
    def execute(
        trade: Trade,
        target_price: float,
        exit_quantity: int,
        current_price: float,
    ):
        """
        Execute a partial exit.

        Returns
        -------
        bool
            True if a partial exit occurred.
        """

        if trade.status != "OPEN":
            return False

        if exit_quantity <= 0:
            return False

        if exit_quantity >= trade.quantity:
            return False

        #
        # LONG
        #
        if trade.direction == "LONG":

            if current_price < target_price:
                return False

        #
        # SHORT
        #
        elif trade.direction == "SHORT":

            if current_price > target_price:
                return False

        else:
            return False

        trade.quantity -= exit_quantity

        return True
