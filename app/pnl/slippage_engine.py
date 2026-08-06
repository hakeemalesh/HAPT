"""
HAPT Slippage Engine
--------------------

Calculates execution slippage for supported
futures contracts.

The default model assumes one tick of slippage
per completed trade.

Future versions will support configurable
entry and exit slippage.
"""

from app.pnl.tick_value_engine import (
    TickValueEngine,
)


class SlippageEngine:
    """Calculates trade slippage."""

    DEFAULT_SLIPPAGE_TICKS = 1

    @classmethod
    def calculate(
        cls,
        symbol,
        quantity=1,
        slippage_ticks=None,
    ):
        """
        Calculate slippage cost.

        Parameters
        ----------
        symbol : str

        quantity : int

        slippage_ticks : int | None

        Returns
        -------
        float
        """

        if slippage_ticks is None:
            slippage_ticks = (
                cls.DEFAULT_SLIPPAGE_TICKS
            )

        tick_value = (
            TickValueEngine.get_tick_value(
                symbol
            )
        )

        cost = (
            slippage_ticks
            * tick_value
            * quantity
        )

        return round(
            cost,
            2,
        )
