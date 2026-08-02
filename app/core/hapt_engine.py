"""
HAPT Engine
-----------

Central orchestration engine for the
Hybrid AI Trading Platform.
"""

from app.market.market_manager import MarketManager
from app.scanner.market_scanner import MarketScanner
from app.strategy.strategy_engine import StrategyEngine
from app.ai.ai_engine import AIEngine

from app.datafeed.market_data import MarketData
from app.pipeline.data_pipeline import DataPipeline

from app.brokers.paper_broker import PaperBroker
from app.execution.execution_engine import ExecutionEngine
from app.journal.trade_journal import TradeJournal
from app.ui.trade_display import TradeDisplay

from app.core.logger import setup_logger


class HAPTEngine:
    """
    Coordinates the complete HAPT workflow.
    """

    def __init__(self):
        """Initialize every HAPT module."""

        self.logger = setup_logger()

        self.market = MarketManager()

        self.scanner = MarketScanner()

        self.strategy = StrategyEngine()

        self.ai = AIEngine()

        self.market_data = MarketData()

        self.pipeline = DataPipeline()

        self.broker = PaperBroker()

        self.execution = ExecutionEngine(
            self.broker
        )

        self.journal = TradeJournal()

        self.display = TradeDisplay()

    def run(self):
    """
    Execute one complete HAPT cycle.
    """

    self.logger.info(
        "Starting HAPT Engine."
    )

    self.broker.connect()

    try:

        #
        # Remaining orchestration
        # will be migrated here
        # in future sprints.
        #
        pass

    finally:

        self.broker.disconnect()

        self.logger.info(
            "HAPT Engine finished."
        )