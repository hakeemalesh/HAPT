"""
HAPT Backtesting Engine
-----------------------

Replays historical market data through the HAPT trading pipeline.
"""

from app.journal.trade_journal import TradeJournal
from app.strategy.strategy_engine import StrategyEngine


class BacktestEngine:
    """Runs a trading strategy against historical candle data."""

    def __init__(self, strategy_engine: StrategyEngine):
        self.strategy_engine = strategy_engine

    def run(self, candles) -> TradeJournal:
        """Replay historical candles."""

        journal = TradeJournal()

        for candle in candles:
            trade = self.strategy_engine.analyze(
    context=candle,
    entry_price=candle["close"],
)

            if trade is not None:
                journal.add_trade(trade)

        return journal
