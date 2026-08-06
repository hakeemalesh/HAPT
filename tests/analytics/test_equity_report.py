"""
Tests for the HAPT Professional Equity Report.
"""

from app.analytics.equity_report import EquityReport


def test_equity_report_contains_all_sections():
    """Report should contain all major sections."""

    report = EquityReport.build(
        starting_balance=10000.00,
        ending_balance=10850.00,
        portfolio_stats={
            "net_profit": 850.00,
            "total_trades": 20,
            "win_rate": 65.0,
            "loss_rate": 35.0,
            "profit_factor": 2.10,
            "expectancy": 42.50,
        },
        drawdown_stats={
            "max_drawdown": 275.00,
            "current_drawdown": 50.00,
        },
        streak_stats={
            "longest_win_streak": 5,
            "longest_loss_streak": 2,
        },
        distribution_stats={
            "largest_win": 220.00,
            "largest_loss": -110.00,
            "average_win": 95.00,
            "average_loss": 45.00,
        },
    )

    assert "HAPT EQUITY REPORT" in report
    assert "Portfolio" in report
    assert "Performance" in report
    assert "Risk" in report
    assert "Trade Behaviour" in report


def test_report_contains_key_values():
    """Report should include supplied values."""

    report = EquityReport.build(
        starting_balance=10000.00,
        ending_balance=10850.00,
        portfolio_stats={
            "net_profit": 850.00,
            "total_trades": 20,
            "win_rate": 65.0,
            "loss_rate": 35.0,
            "profit_factor": 2.10,
            "expectancy": 42.50,
        },
        drawdown_stats={
            "max_drawdown": 275.00,
            "current_drawdown": 50.00,
        },
        streak_stats={
            "longest_win_streak": 5,
            "longest_loss_streak": 2,
        },
        distribution_stats={
            "largest_win": 220.00,
            "largest_loss": -110.00,
            "average_win": 95.00,
            "average_loss": 45.00,
        },
    )

    assert "$10,000.00" in report
    assert "$10,850.00" in report
    assert "$850.00" in report
    assert "65.00%" in report
    assert "2.10" in report
    assert "$275.00" in report
    assert "$220.00" in report
    assert "$-110.00" in report
