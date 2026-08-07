"""
Builds a complete executable trade plan from
market context using the Strategy Engine.
"""

from app.models.trade import Trade
from app.strategy.strategy_engine import StrategyEngine


class TradePlanner:
    """
    Builds a complete trade plan ready for execution.
    """

    def __init__(self) -> None:
        """Initialize planner dependencies."""

        self.strategy: StrategyEngine = StrategyEngine()

    def create_trade_plan(
        self,
        market_context: dict,
        entry_price: float,
    ) -> Trade:
        """
        Build a complete trade plan.

        Parameters
        ----------
        market_context : dict
            Market analysis context.

        entry_price : float
            Current market price.

        Returns
        -------
        Trade
            Completed trade plan.
        """

        trade = self.strategy.analyze(
            context=market_context,
            entry_price=entry_price,
        )

        return trade