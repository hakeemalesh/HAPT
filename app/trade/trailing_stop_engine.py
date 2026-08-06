"""
HAPT Trailing Stop Engine
-------------------------

Moves a trade's stop-loss in the direction
of profit only.
"""

from app.trade.trade import Trade


class TrailingStopEngine:
    """Updates a trade's trailing stop."""

    @staticmethod
    def update(
        trade: Trade,
        trail_distance: float,
        current_price: float,
    ):
        """
        Update the trailing stop.

        Parameters
        ----------
        trade : Trade

        trail_distance : float

        current_price : float

        Returns
        -------
        bool
            True if stop-loss changed.
        """

        if (
            trade.status != "OPEN"
            or trade.stop_loss is None
        ):
            return False

        if trade.direction == "LONG":

            new_stop = (
                current_price - trail_distance
            )

            if new_stop > trade.stop_loss:
                trade.stop_loss = new_stop
                return True

        elif trade.direction == "SHORT":

            new_stop = (
                current_price + trail_distance
            )

            if new_stop < trade.stop_loss:
                trade.stop_loss = new_stop
                return True

        return False
