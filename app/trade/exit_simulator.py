"""
HAPT Complete Exit Simulator
----------------------------

Coordinates all trade management engines.

Execution order:

1. Break-even
2. Trailing Stop
3. Partial Profit
4. Stop Loss
5. Take Profit
"""

from app.trade.breakeven_engine import BreakEvenEngine
from app.trade.partial_profit_engine import PartialProfitEngine
from app.trade.stop_loss_engine import StopLossEngine
from app.trade.take_profit_engine import TakeProfitEngine
from app.trade.trade import Trade
from app.trade.trailing_stop_engine import TrailingStopEngine


class ExitSimulator:
    """Coordinates trade management."""

    @staticmethod
    def process_candle(
        trade: Trade,
        candle: dict,
        *,
        trail_distance: float | None = None,
        break_even_trigger: float | None = None,
        partial_target: float | None = None,
        partial_quantity: int | None = None,
    ) -> Trade:
        """
        Process one replay candle.

        Parameters
        ----------
        trade : Trade

        candle : dict
            Must contain:
                high
                low
                close
                timestamp

        Returns
        -------
        Trade
            Updated trade object.
        """

        current_price = candle["close"]

        #
        # Break-even
        #
        if break_even_trigger is not None:

            BreakEvenEngine.update(
                trade=trade,
                trigger_distance=break_even_trigger,
                current_price=current_price,
            )

        #
        # Trailing stop
        #
        if trail_distance is not None:

            TrailingStopEngine.update(
                trade=trade,
                trail_distance=trail_distance,
                current_price=current_price,
            )

        #
        # Partial profit
        #
        if (
            partial_target is not None
            and partial_quantity is not None
        ):

            PartialProfitEngine.execute(
                trade=trade,
                target_price=partial_target,
                exit_quantity=partial_quantity,
                current_price=current_price,
            )

        #
        # Exit checks
        #
        StopLossEngine.evaluate(
            trade,
            candle,
        )

        if trade.status == "OPEN":

            TakeProfitEngine.evaluate(
                trade,
                candle,
            )

        return trade
