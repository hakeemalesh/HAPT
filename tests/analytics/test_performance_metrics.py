"""
Tests for the HAPT Performance Metrics Engine.
"""

from app.analytics.performance_metrics import (
    PerformanceMetrics,
)


def test_empty_trade_list():
    """Empty trade list."""

    result = PerformanceMetrics.calculate([])

    assert result["total_trades"] == 0
    assert result["winning_trades"] == 0
    assert result["losing_trades"] == 0
    assert result["breakeven_trades"] == 0
    assert result["gross_profit"] == 0
    assert result["gross_loss"] == 0
    assert result["net_profit"] == 0
    assert result["win_rate"] == 0
    assert result["loss_rate"] == 0
    assert result["average_winner"] == 0
    assert result["average_loser"] == 0
    assert result["largest_winner"] == 0
    assert result["largest_loser"] == 0
    assert result["profit_factor"] == 0


def test_single_winner():
    """Single winning trade."""

    trades = [
        {"net_pnl": 100.00},
    ]

    result = PerformanceMetrics.calculate(trades)

    assert result["total_trades"] == 1
    assert result["winning_trades"] == 1
    assert result["losing_trades"] == 0
    assert result["win_rate"] == 100.00
    assert result["loss_rate"] == 0.00
    assert result["gross_profit"] == 100.00
    assert result["gross_loss"] == 0.00
    assert result["net_profit"] == 100.00
    assert result["average_winner"] == 100.00
    assert result["average_loser"] == 0.00
    assert result["largest_winner"] == 100.00
    assert result["largest_loser"] == 0.00
    assert result["profit_factor"] == 0.00


def test_single_loser():
    """Single losing trade."""

    trades = [
        {"net_pnl": -50.00},
    ]

    result = PerformanceMetrics.calculate(trades)

    assert result["total_trades"] == 1
    assert result["winning_trades"] == 0
    assert result["losing_trades"] == 1
    assert result["win_rate"] == 0.00
    assert result["loss_rate"] == 100.00
    assert result["gross_profit"] == 0.00
    assert result["gross_loss"] == 50.00
    assert result["net_profit"] == -50.00
    assert result["average_winner"] == 0.00
    assert result["average_loser"] == 50.00
    assert result["largest_winner"] == 0.00
    assert result["largest_loser"] == -50.00
    assert result["profit_factor"] == 0.00


def test_mixed_results():
    """Mixed winners, losers and breakeven."""

    trades = [
        {"net_pnl": 100.00},
        {"net_pnl": 50.00},
        {"net_pnl": -40.00},
        {"net_pnl": -10.00},
        {"net_pnl": 0.00},
    ]

    result = PerformanceMetrics.calculate(trades)

    assert result["total_trades"] == 5
    assert result["winning_trades"] == 2
    assert result["losing_trades"] == 2
    assert result["breakeven_trades"] == 1

    assert result["win_rate"] == 40.00
    assert result["loss_rate"] == 40.00

    assert result["gross_profit"] == 150.00
    assert result["gross_loss"] == 50.00
    assert result["net_profit"] == 100.00

    assert result["average_winner"] == 75.00
    assert result["average_loser"] == 25.00

    assert result["largest_winner"] == 100.00
    assert result["largest_loser"] == -40.00

    assert result["profit_factor"] == 3.00


def test_all_breakeven():
    """All trades breakeven."""

    trades = [
        {"net_pnl": 0.00},
        {"net_pnl": 0.00},
    ]

    result = PerformanceMetrics.calculate(trades)

    assert result["total_trades"] == 2
    assert result["winning_trades"] == 0
    assert result["losing_trades"] == 0
    assert result["breakeven_trades"] == 2

    assert result["gross_profit"] == 0
    assert result["gross_loss"] == 0
    assert result["net_profit"] == 0

    assert result["win_rate"] == 0
    assert result["loss_rate"] == 0

    assert result["average_winner"] == 0
    assert result["average_loser"] == 0

    assert result["largest_winner"] == 0
    assert result["largest_loser"] == 0

    assert result["profit_factor"] == 0
