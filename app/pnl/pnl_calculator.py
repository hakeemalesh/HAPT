"""
HAPT Profit & Loss Calculator
-----------------------------

Calculates gross and net futures profit/loss.

Uses the TickValueEngine and CommissionEngine so
results reflect contract specifications and
trading costs.

Slippage and exchange fees will be added in
later nodes.
"""

from app.pnl.commission_engine import (
    CommissionEngine,
)
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
        Calculate futures trade P&L.

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

        tick_value = TickValueEngine.get_tick_value(
            symbol
        )

        gross_pnl = round(
            ticks * tick_value * quantity,
            2,
        )

        commission = CommissionEngine.calculate(
            symbol,
            quantity,
        )

        net_pnl = round(
            gross_pnl - commission,
            2,
        )

        return {
            "symbol": symbol,
            "direction": direction,
            "ticks": ticks,
            "tick_value": tick_value,
            "quantity": quantity,
            "gross_pnl": gross_pnl,
            "commission": commission,
            "net_pnl": net_pnl,
        }
