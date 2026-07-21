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


def main():
    """Start the HAPT application."""

    logger = setup_logger()

    show_banner()

    run_startup_checks()

    # Initialize modules
    market = MarketManager()
    scanner = MarketScanner()
    strategy = StrategyEngine()
    ai = AIEngine()
    journal = TradeJournal()
    data = MarketData()

    # Load watchlist
    market.load_default_watchlist()
    symbols = market.get_symbols()

    # Scan market
    scanner.load_symbols(symbols)
    scanner.scan()

    # Analyze each symbol
    for symbol in symbols:

        price = data.get_price(symbol)
        print(f"Current price of {symbol}: {price}")

        strategy_result = strategy.analyze(symbol)
        ai_result = ai.analyze(strategy_result)

        journal.record_trade(ai_result)

    logger.info("HAPT completed one market scan successfully.")


if __name__ == "__main__":
    main()