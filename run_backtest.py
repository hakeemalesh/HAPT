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


def print_distribution(title, data):
    """Print a distribution table."""

    print(title)
    print("-" * len(title))

    if not data:
        print("None")
        print()
        return

    for key in sorted(data):
        print(f"{key:<25} : {data[key]}")

    print()


def print_rejection_reasons(data):
    """Print rejection reasons ordered by frequency."""

    print("Top Rejection Reasons")
    print("---------------------")

    if not data:
        print("None")
        print()
        return

    for reason, count in sorted(
        data.items(),
        key=lambda item: item[1],
        reverse=True,
    ):
        print(f"{reason:<25} : {count}")

    print()


def main():
    """Program entry point."""

    args = build_parser().parse_args()

    market = MarketData(provider=args.provider)

    candles = market.get_historical_data(args.symbol)

    print("=" * 60)
    print("HAPT PROFESSIONAL BACKTEST REPORT")
    print("=" * 60)
    print()

    print(f"Provider             : {args.provider}")
    print(f"Symbol               : {args.symbol}")
    print(f"Historical Candles   : {len(candles)}")
    print()

    if not candles:
        print("No historical data available.")
        return

    runner = ReplayRunner()

    journal = runner.run(
        args.symbol,
        candles,
    )

    analyzer = PerformanceAnalyzer(journal)

    summary = analyzer.summary()

    print("Performance")
    print("-----------")
    print(
        f"Trades Evaluated     : {summary['total_trades']}"
    )
    print(
        f"Approved Trades      : {summary['approved_trades']}"
    )
    print(
        f"Rejected Trades      : {summary['rejected_trades']}"
    )
    print(
        f"Approval Rate        : "
        f"{summary['approval_rate']:.2f}%"
    )
    print(
        f"Average Risk/Reward  : "
        f"{summary['average_risk_reward']:.2f}"
    )
    print()

    print_distribution(
        "Signal Distribution",
        summary["signal_distribution"],
    )

    print_distribution(
        "Grade Distribution",
        summary["grade_distribution"],
    )

    print_rejection_reasons(
        summary["rejection_reasons"],
    )

    print("=" * 60)


if __name__ == "__main__":
    main()
