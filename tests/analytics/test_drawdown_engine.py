"""
Tests for the HAPT Drawdown Engine.
"""

from app.analytics.drawdown_engine import DrawdownEngine


def test_empty_equity_curve():
    """Empty equity curve."""

    stats = DrawdownEngine.calculate([])

    assert stats["peak"] == 0.0
    assert stats["current_drawdown"] == 0.0
    assert stats["max_drawdown"] == 0.0
    assert stats["max_drawdown_pct"] == 0.0


def test_monotonic_growth():
    """No drawdown during continuous growth."""

    stats = DrawdownEngine.calculate(
        [
            10000.00,
            10100.00,
            10300.00,
            10500.00,
        ]
    )

    assert stats["peak"] == 10500.00
    assert stats["current_drawdown"] == 0.0
    assert stats["max_drawdown"] == 0.0
    assert stats["max_drawdown_pct"] == 0.0


def test_single_drawdown():
    """Single drawdown."""

    stats = DrawdownEngine.calculate(
        [
            10000.00,
            10500.00,
            10300.00,
        ]
    )

    assert stats["peak"] == 10500.00
    assert stats["current_drawdown"] == 200.00
    assert stats["max_drawdown"] == 200.00
    assert stats["max_drawdown_pct"] == 1.90


def test_multiple_drawdowns():
    """Largest drawdown should be reported."""

    stats = DrawdownEngine.calculate(
        [
            10000.00,
            10400.00,
            10250.00,
            10600.00,
            10100.00,
            10800.00,
        ]
    )

    assert stats["peak"] == 10800.00
    assert stats["current_drawdown"] == 0.00
    assert stats["max_drawdown"] == 500.00
    assert stats["max_drawdown_pct"] == 4.63


def test_recovery_to_new_high():
    """Recovery should reset current drawdown."""

    stats = DrawdownEngine.calculate(
        [
            10000.00,
            10300.00,
            10100.00,
            10450.00,
        ]
    )

    assert stats["peak"] == 10450.00
    assert stats["current_drawdown"] == 0.00
    assert stats["max_drawdown"] == 200.00
    assert stats["max_drawdown_pct"] == 1.91
