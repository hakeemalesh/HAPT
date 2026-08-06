"""
HAPT Stop Loss Engine
---------------------

Evaluates whether a stop-loss has been hit.
"""

from app.trade.trade import Trade


class StopLossEngine:
    """Evaluates stop-loss exits."""

    @staticmethod
    def evaluate(
        trade: Trade,
        candle: dict,
    ):
        """
        Evaluate one candle against a trade's stop-loss.

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
            True if the stop-loss was triggered.
        """

        if (
            trade.status != "OPEN"
            or trade.stop_loss is None
        ):
            return False

        if trade.direction == "LONG":

            if candle["low"] <= trade.stop_loss:

                trade.exit_price = trade.stop_loss
                trade.exit_time = candle.get(
                    "timestamp"
                )
                trade.exit_reason = "Stop Loss"
                trade.status = "CLOSED"

                return True

        elif trade.direction == "SHORT":

            if candle["high"] >= trade.stop_loss:

                trade.exit_price = trade.stop_loss
                trade.exit_time = candle.get(
                    "timestamp"
                )
                trade.exit_reason = "Stop Loss"
                trade.status = "CLOSED"

                return True

        return False
