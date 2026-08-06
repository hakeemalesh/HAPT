"""
HAPT Take Profit Engine
-----------------------

Evaluates whether a take-profit has been hit.
"""

from app.trade.trade import Trade


class TakeProfitEngine:
    """Evaluates take-profit exits."""

    @staticmethod
    def evaluate(
        trade: Trade,
        candle: dict,
    ):
        """
        Evaluate one candle against a trade's
        take-profit.

        Parameters
        ----------
        trade : Trade

        candle : dict
            Expected keys:
            high
            low
            close
            timestamp

        Returns
        -------
        bool
            True if take-profit was triggered.
        """

        if (
            trade.status != "OPEN"
            or trade.take_profit is None
        ):
            return False

        if trade.direction == "LONG":

            if candle["high"] >= trade.take_profit:

                trade.exit_price = (
                    trade.take_profit
                )
                trade.exit_time = candle.get(
                    "timestamp"
                )
                trade.exit_reason = (
                    "Take Profit"
                )
                trade.status = "CLOSED"

                return True

        elif trade.direction == "SHORT":

            if candle["low"] <= trade.take_profit:

                trade.exit_price = (
                    trade.take_profit
                )
                trade.exit_time = candle.get(
                    "timestamp"
                )
                trade.exit_reason = (
                    "Take Profit"
                )
                trade.status = "CLOSED"

                return True

        return False
