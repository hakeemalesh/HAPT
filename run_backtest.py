#!/usr/bin/env python3
"""
HAPT Backtest Runner
--------------------

Command-line entry point for executing HAPT backtests.
"""

import argparse

from app.analytics.performance_analyzer import PerformanceAnalyzer
from app.datafeed.market_data import MarketData
from app.replay.replay_runner import ReplayRunner


def build_parser():
    """Create the command-line argument parser."""

    parser = argparse.ArgumentParser(
        description="Run a HAPT historical backtest."
    )

    parser.add_argument(
        "--symbol",
        required=True,
        help="Market symbol (e.g. MES, MNQ, ES).",
    )

    parser.add_argument(
        "--provider",
        default="demo",
        choices=["demo", "yahoo"],
        help="Historical data provider.",
    )

    return parser


def main():
    """Program entry point."""

    args = build_parser().parse_args()

    market = MarketData(provider=args.provider)

    candles = market.get_historical_data(args.symbol)

    print("=" * 50)
    print("HAPT Professional Opportunity Engine")
    print("=" * 50)
    print(f"Provider : {args.provider}")
    print(f"Symbol   : {args.symbol}")
    print(f"Candles  : {len(candles)}")
    print()

    if not candles:
        print("No historical data found.")
        return

    print("Running replay...")

    runner = ReplayRunner()

    journal = runner.run(
        args.symbol,
        candles,
    )

    analyzer = PerformanceAnalyzer(journal)

    print("Replay completed.")
    print()
    print(f"Trades generated : {journal.count()}")
    print(f"Approved trades  : {analyzer.approved_trades()}")
    print(f"Rejected trades  : {analyzer.rejected_trades()}")


if __name__ == "__main__":
    main()
