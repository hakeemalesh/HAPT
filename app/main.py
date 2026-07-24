"""
HAPT Main Entry Point
---------------------

Starts the Hybrid AI Trading Platform.
"""


from core.banner import show_banner
from core.logger import setup_logger
from core.startup import run_startup_checks


from market.market_manager import MarketManager
from scanner.market_scanner import MarketScanner
from strategy.strategy_engine import StrategyEngine
from ai.ai_engine import AIEngine
from journal.trade_journal import TradeJournal

from datafeed.market_data import MarketData
from pipeline.data_pipeline import DataPipeline

from brokers.paper_broker import PaperBroker
from ui.trade_display import TradeDisplay



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


        print(
            f"Current price of {symbol}: {price}"
        )



        # Build complete market intelligence context

        market_context = pipeline.build_context(symbol)



        if market_context is None:

            print(
                f"No historical data available for {symbol}"
            )

            continue



        strategy_result = strategy.analyze(
            symbol,
            price,
            market_context
        )


        ai_result = ai.analyze(
            strategy_result
        )



        # Display trade setup

        display.show(
            strategy_result
        )



        # Record trade

        journal.record_trade(
            ai_result
        )



    logger.info(
        "HAPT completed one market scan successfully."
    )



if __name__ == "__main__":

    main()