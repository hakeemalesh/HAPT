"""
HAPT Main Entry Point
---------------------

Starts the Hybrid AI Trading Platform.
"""

from app.core.banner import show_banner
from app.core.logger import setup_logger
from app.core.startup import run_startup_checks

from app.market.market_manager import MarketManager
from app.scanner.market_scanner import MarketScanner
from app.strategy.strategy_engine import StrategyEngine
from app.ai.ai_engine import AIEngine
from app.journal.trade_journal import TradeJournal

from app.datafeed.market_data import MarketData
from app.pipeline.data_pipeline import DataPipeline

from app.brokers.paper_broker import PaperBroker
from app.ui.trade_display import TradeDisplay


def main():
    """Start the HAPT application."""

    logger = setup_logger()

    show_banner()

    run_startup_checks()

    # --------------------------------------------------
    # Initialize HAPT Modules
    # --------------------------------------------------

    market = MarketManager()
    scanner = MarketScanner()
    strategy = StrategyEngine()
    ai = AIEngine()
    journal = TradeJournal()
    data = MarketData()
    pipeline = DataPipeline()
    broker = PaperBroker()
    display = TradeDisplay()

    # --------------------------------------------------
    # Connect Broker
    # --------------------------------------------------

    broker.connect()

    # --------------------------------------------------
    # Load Watchlist
    # --------------------------------------------------

    market.load_default_watchlist()
    symbols = market.get_symbols()

    # --------------------------------------------------
    # Market Scanner
    # --------------------------------------------------

    scanner.load_symbols(symbols)
    scanner.scan()

    # --------------------------------------------------
    # Analyze Market
    # --------------------------------------------------

    for symbol in symbols:

        price = data.get_price(symbol)

        if price is None:
            logger.warning(
                "No current price available for %s",
                symbol,
            )
            continue

        print(f"Current price of {symbol}: {price}")

        # Build complete market intelligence context
        market_context = pipeline.build_context(symbol)

        if market_context is None:
            print(f"No historical data available for {symbol}")
            continue

        # --------------------------------------------------
        # Run Strategy Engine
        # --------------------------------------------------

        strategy_result = strategy.analyze(
            market_context,
            price,
        )

        # --------------------------------------------------
        # AI Validation
        # --------------------------------------------------

        ai_result = ai.analyze(strategy_result)

        # --------------------------------------------------
        # Display Trade
        # --------------------------------------------------

        display.show(strategy_result)

        # --------------------------------------------------
        # Journal
        # --------------------------------------------------

        journal.record_trade(ai_result)

    logger.info(
        "HAPT completed one market scan successfully."
    )


if __name__ == "__main__":
    main()