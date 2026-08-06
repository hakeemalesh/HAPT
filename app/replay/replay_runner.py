"""
HAPT Replay Runner
------------------

Runs a complete historical replay using the
production HAPT trading pipeline.

Responsibilities
----------------
1. Request historical contexts from ReplayController.
2. Execute the production StrategyEngine.
3. Record resulting trades in the TradeJournal.
"""

from app.journal.trade_journal import TradeJournal
from app.replay.replay_controller import ReplayController
from app.strategy.strategy_engine import StrategyEngine


class ReplayRunner:
    """
    Runs a complete historical replay.
    """

    def __init__(
        self,
        replay_controller=None,
        strategy_engine=None,
    ):
        """Initialize replay runner."""

        self.replay_controller = (
            replay_controller
            if replay_controller is not None
            else ReplayController()
        )

        self.strategy_engine = (
            strategy_engine
            if strategy_engine is not None
            else StrategyEngine()
        )

    def run(
        self,
        candles,
    ) -> TradeJournal:
        """
        Execute a complete replay.

        Parameters
        ----------
        candles : list
            Historical candle data.

        Returns
        -------
        TradeJournal
            Journal containing all generated trades.
        """

        journal = TradeJournal()

        self.replay_controller.load(candles)

        while self.replay_controller.has_next():

            context = self.replay_controller.next_context()

            if context is None:
                continue

            trade = self.strategy_engine.analyze(
                context=context,
                entry_price=context["price"],
            )

            journal.add_trade(trade)

        return journal
