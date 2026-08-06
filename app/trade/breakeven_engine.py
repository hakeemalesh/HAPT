"""
HAPT Break-even Stop Engine
---------------------------

Moves the stop-loss to the entry price once
a configurable trigger has been reached.
"""

from app.trade.trade import Trade


class BreakEvenEngine:
    """Moves stop-loss to break-even."""

    @staticmethod
    def update(
        trade: Trade,
        trigger_distance: float,
        current_price: float,
    ):
        """
        Update a trade to break-even.

        Parameters
        ----------
        trade : Trade

        trigger_distance : float
            Distance required before moving stop.

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

        #
        # LONG
        #
        if trade.direction == "LONG":

            trigger = (
                trade.entry_price
                + trigger_distance
            )

            if (
                current_price >= trigger
                and trade.stop_loss
                < trade.entry_price
            ):

                trade.stop_loss = (
                    trade.entry_price
                )

                return True

        #
        # SHORT
        #
        elif trade.direction == "SHORT":

            trigger = (
                trade.entry_price
                - trigger_distance
            )

            if (
                current_price <= trigger
                and trade.stop_loss
                > trade.entry_price
            ):

                trade.stop_loss = (
                    trade.entry_price
                )

                return True

        return False
