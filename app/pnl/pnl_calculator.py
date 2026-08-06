"""
HAPT Profit & Loss Calculator
-----------------------------

Calculates gross futures profit and loss.

Uses the TickValueEngine so calculations are based
on the correct futures contract specifications.

Commission, slippage and fees are intentionally
excluded from this component and will be introduced
in later nodes.
"""

from app.pnl.tick_value_engine import (
    TickValueEngine,
)


class PnLCalculator:
    """Calculates futures trade profit and loss."""

    @staticmethod
    def calculate(
        symbol,
        entry_price,
        exit_price,
        quantity=1,
        direction="LONG",
    ):
        """
        Calculate gross futures P&L.

        Parameters
        ----------
        symbol : str

        entry_price : float

        exit_price : float

        quantity : int

        direction : str
            LONG or SHORT

        Returns
        -------
        dict
        """

        if direction not in (
            "LONG",
            "SHORT",
        ):
            raise ValueError(
                "direction must be LONG or SHORT."
            )

        ticks = TickValueEngine.calculate_ticks(
            symbol=symbol,
            entry_price=entry_price,
            exit_price=exit_price,
        )

        if direction == "SHORT":
            ticks *= -1

        tick_value = (
            TickValueEngine.get_tick_value(
                symbol
            )
        )

        gross_pnl = (
            ticks
            * tick_value
            * quantity
        )

        return {
            "symbol": symbol,
            "direction": direction,
            "ticks": ticks,
            "tick_value": tick_value,
            "quantity": quantity,
            "gross_pnl": gross_pnl,
        }
