"""
Tests for the HAPT Portfolio Statistics Engine.
"""

from app.analytics.portfolio_statistics import PortfolioStatistics


def test_empty_trade_history():
    """No completed trades."""

    stats = PortfolioStatistics.calculate([])

    assert stats["total_trades"] == 0
    assert stats["winning_trades"] == 0
    assert stats["losing_trades"] == 0
    assert stats["breakeven_trades"] == 0
    assert stats["net_profit"] == 0.0
    assert stats["profit_factor"] == 0.0
    assert stats["expectancy"] == 0.0


def test_all_winning_trades():
    """Only winning trades."""

    stats = PortfolioStatistics.calculate(
        [100.0, 200.0, 300.0]
    )

    assert stats["total_trades"] == 3
    assert stats["winning_trades"] == 3
    assert stats["losing_trades"] == 0
    assert stats["win_rate"] == 100.0
    assert stats["gross_profit"] == 600.0
    assert stats["gross_loss"] == 0.0
    assert stats["net_profit"] == 600.0
    assert stats["average_win"] == 200.0
    assert stats["largest_win"] == 300.0


def test_all_losing_trades():
    """Only losing trades."""

    stats = PortfolioStatistics.calculate(
        [-100.0, -50.0]
    )

    assert stats["total_trades"] == 2
    assert stats["winning_trades"] == 0
    assert stats["losing_trades"] == 2
    assert stats["loss_rate"] == 100.0
    assert stats["gross_profit"] == 0.0
    assert stats["gross_loss"] == 150.0
    assert stats["net_profit"] == -150.0
    assert stats["average_loss"] == 75.0
    assert stats["largest_loss"] == -100.0


def test_mixed_trade_results():
    """Mixed winning, losing and break-even trades."""

    stats = PortfolioStatistics.calculate(
        [
            200.0,
            -100.0,
            0.0,
            300.0,
            -50.0,
        ]
    )

    assert stats["total_trades"] == 5
    assert stats["winning_trades"] == 2
    assert stats["losing_trades"] == 2
    assert stats["breakeven_trades"] == 1

    assert stats["gross_profit"] == 500.0
    assert stats["gross_loss"] == 150.0
    assert stats["net_profit"] == 350.0

    assert stats["average_win"] == 250.0
    assert stats["average_loss"] == 75.0

    assert stats["largest_win"] == 300.0
    assert stats["largest_loss"] == -100.0

    assert stats["profit_factor"] == 3.33
    assert stats["expectancy"] == 70.0


def test_win_and_loss_rates():
    """Rates should be calculated correctly."""

    stats = PortfolioStatistics.calculate(
        [
            100.0,
            50.0,
            -20.0,
            -10.0,
        ]
    )

    assert stats["win_rate"] == 50.0
    assert stats["loss_rate"] == 50.0


def test_break_even_only():
    """Only break-even trades."""

    stats = PortfolioStatistics.calculate(
        [0.0, 0.0, 0.0]
    )

    assert stats["breakeven_trades"] == 3
    assert stats["winning_trades"] == 0
    assert stats["losing_trades"] == 0
    assert stats["gross_profit"] == 0.0
    assert stats["gross_loss"] == 0.0
    assert stats["net_profit"] == 0.0
