"""
HAPT Profit & Loss Calculator
-----------------------------

Calculates gross and net futures profit/loss.

Includes:
- Tick Value
- Commission
- Slippage

Future versions will include exchange fees,
borrowing costs and taxes where applicable.
"""

from app.pnl.commission_engine import CommissionEngine
from app.pnl.slippage_engine import SlippageEngine
from app.pnl.tick_value_engine import TickValueEngine


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
        """Calculate complete trade P&L."""

        if direction not in ("LONG", "SHORT"):
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

        slippage = SlippageEngine.calculate(
            symbol,
            quantity,
        )

        net_pnl = round(
            gross_pnl
            - commission
            - slippage,
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
            "slippage": slippage,
            "net_pnl": net_pnl,
        }
