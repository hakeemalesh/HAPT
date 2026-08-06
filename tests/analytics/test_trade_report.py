"""
Tests for the HAPT Professional Trade Report.
"""

from app.analytics.trade_report import TradeReport


def test_report_generation():
    """Professional report should contain key metrics."""

    metrics = {
        "total_trades": 100,
        "winning_trades": 60,
        "losing_trades": 35,
        "breakeven_trades": 5,
        "win_rate": 60.0,
        "loss_rate": 35.0,
        "gross_profit": 12500.50,
        "gross_loss": 5200.25,
        "net_profit": 7300.25,
        "profit_factor": 2.40,
        "average_winner": 208.34,
        "average_loser": 148.58,
        "largest_winner": 950.00,
        "largest_loser": -420.00,
    }

    report = TradeReport.generate(metrics)

    assert isinstance(report, str)

    assert "HAPT PROFESSIONAL PERFORMANCE REPORT" in report

    assert "Total Trades" in report
    assert "Winning Trades" in report
    assert "Losing Trades" in report
    assert "Breakeven Trades" in report

    assert "Gross Profit" in report
    assert "Gross Loss" in report
    assert "Net Profit" in report

    assert "Profit Factor" in report

    assert "Average Winner" in report
    assert "Average Loser" in report

    assert "Largest Winner" in report
    assert "Largest Loser" in report


def test_empty_metrics():
    """Report should support zero values."""

    metrics = {
        "total_trades": 0,
        "winning_trades": 0,
        "losing_trades": 0,
        "breakeven_trades": 0,
        "win_rate": 0.0,
        "loss_rate": 0.0,
        "gross_profit": 0.0,
        "gross_loss": 0.0,
        "net_profit": 0.0,
        "profit_factor": 0.0,
        "average_winner": 0.0,
        "average_loser": 0.0,
        "largest_winner": 0.0,
        "largest_loser": 0.0,
    }

    report = TradeReport.generate(metrics)

    assert "0.00" in report
    assert "Total Trades" in report
