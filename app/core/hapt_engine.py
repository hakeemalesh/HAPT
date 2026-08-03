"""
HAPT Engine
-----------

Central orchestration engine for the
Hybrid AI Trading Platform.

This class coordinates every major
production module while keeping
business logic inside the individual
engines.
"""

from app.core.logger import setup_logger

from app.market.market_manager import MarketManager
from app.scanner.market_scanner import MarketScanner

from app.strategy.strategy_engine import StrategyEngine
from app.ai.ai_engine import AIEngine

from app.datafeed.market_data import MarketData
from app.pipeline.data_pipeline import DataPipeline

from app.brokers.paper_broker import PaperBroker
from app.execution.execution_engine import ExecutionEngine

from app.trade_planner.trade_planner import TradePlanner
from app.trade_validator.trade_validator import TradeValidator

from app.journal.trade_journal import TradeJournal
from app.ui.trade_display import TradeDisplay


class HAPTEngine:
    """
    Coordinates the complete HAPT
    production workflow.
    """

    def __init__(self):
        """
        Initialize every production
        module used by HAPT.
        """

        self.logger = setup_logger()

        #
        # Market
        #
        self.market = MarketManager()

        self.scanner = MarketScanner()

        self.market_data = MarketData()

        self.pipeline = DataPipeline()

        #
        # Trading Intelligence
        #
        self.strategy = StrategyEngine()

        self.trade_planner = TradePlanner()

        self.trade_validator = TradeValidator()

        self.ai = AIEngine()

        #
        # Execution
        #
        self.broker = PaperBroker()

        self.execution = ExecutionEngine(
            self.broker
        )

        #
        # Recording
        #
        self.journal = TradeJournal()

        self.display = TradeDisplay()

    def run(self):
        """
        Execute one complete HAPT
        market cycle.
        """

        self.logger.info(
            "Starting HAPT Engine."
        )

        self.broker.connect()

        try:

            #
            # Load Watchlist
            #
            self.market.load_default_watchlist()

            symbols = self.market.get_symbols()

            self.logger.info(
                "Loaded %d trading instruments.",
                len(symbols),
            )

            #
            # Scan Market
            #
            self.scanner.load_symbols(
                symbols
            )

            self.scanner.scan()

            #
            # Process Every Symbol
            #
            for symbol in symbols:

                self._process_symbol(
                    symbol
                )

            self.logger.info(
                "Recorded %d trades.",
                self.journal.count(),
            )

        finally:

            self.broker.disconnect()

            self.logger.info(
                "HAPT Engine finished."
            )

    def _process_symbol(
        self,
        symbol: str,
    ) -> None:
        """
        Process one trading symbol through the
        complete HAPT production workflow.
        """

        self.logger.info(
            "Analyzing %s",
            symbol,
        )

        try:

            #
            # Current Market Price
            #
            price = self.market_data.get_price(
                symbol
            )

            if price is None:

                self.logger.warning(
                    "No current price available for %s",
                    symbol,
                )

                return

            self.logger.info(
                "Current price of %s: %s",
                symbol,
                price,
            )

            #
            # Build Market Context
            #
            market_context = self.pipeline.build_context(
                symbol,
                price,
            )

            if market_context is None:

                self.logger.warning(
                    "No historical data available for %s",
                    symbol,
                )

                return

            #
            # Strategy Analysis
            #
            strategy_result = self.strategy.analyze(
                market_context,
                price,
            )

            #
            # Build Trade Plan
            #
            trade = self.trade_planner.create_trade_plan(
                strategy_result
            )

            #
            # Validate Trade
            #
            if not self.trade_validator.validate(
                trade
            ):

                self.logger.info(
                    "Trade rejected for %s",
                    symbol,
                )

                return

            #
            # AI Review
            #
            trade = self.ai.analyze(
                trade
            )

            #
            # Execute Trade
            #
            trade = self.execution.execute(
                trade
            )

            #
            # Display Trade
            #
            self.display.show(
                trade
            )

            #
            # Record Trade
            #
            self.journal.record_trade(
                trade
            )

            self.logger.info(
                "Completed %s",
                symbol,
            )

        except Exception as error:

            self.logger.exception(
                "Failed processing %s: %s",
                symbol,
                error,
            )