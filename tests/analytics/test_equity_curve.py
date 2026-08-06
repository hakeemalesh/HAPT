"""
Tests for the HAPT Equity Curve Engine.
"""

from app.analytics.equity_curve import EquityCurve


def test_empty_trade_results():
    """No trades should return starting balance only."""

    equity = EquityCurve.build(
        starting_balance=10000.00,
        trade_results=[],
    )

    assert equity == [10000.00]


def test_single_winning_trade():
    """One winning trade."""

    equity = EquityCurve.build(
        starting_balance=10000.00,
        trade_results=[250.00],
    )

    assert equity == [
        10000.00,
        10250.00,
    ]


def test_single_losing_trade():
    """One losing trade."""

    equity = EquityCurve.build(
        starting_balance=10000.00,
        trade_results=[-150.00],
    )

    assert equity == [
        10000.00,
        9850.00,
    ]


def test_multiple_trade_results():
    """Multiple trades."""

    equity = EquityCurve.build(
        starting_balance=10000.00,
        trade_results=[
            200.00,
            -100.00,
            300.00,
            -50.00,
        ],
    )

    assert equity == [
        10000.00,
        10200.00,
        10100.00,
        10400.00,
        10350.00,
    ]


def test_rounding():
    """Balances should be rounded to two decimals."""

    equity = EquityCurve.build(
        starting_balance=10000.00,
        trade_results=[
            33.333,
            -10.111,
        ],
    )

    assert equity == [
        10000.00,
        10033.33,
        10023.22,
    ]
