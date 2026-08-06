"""
Tests for the HAPT Portfolio Analytics Dashboard.
"""

from app.analytics.portfolio_dashboard import PortfolioDashboard


def test_dashboard_contains_all_sections():
    """Dashboard should contain every analytics component."""

    dashboard = PortfolioDashboard.build(
        equity_curve=[10000.0, 10100.0, 10250.0],
        portfolio_stats={
            "total_trades": 10,
            "net_profit": 250.0,
        },
        drawdown_stats={
            "max_drawdown": 120.0,
        },
        streak_stats={
            "longest_win_streak": 4,
        },
        distribution_stats={
            "average_win": 95.0,
        },
        report="Sample Report",
    )

    assert "equity_curve" in dashboard
    assert "portfolio" in dashboard
    assert "drawdown" in dashboard
    assert "streaks" in dashboard
    assert "distribution" in dashboard
    assert "report" in dashboard


def test_dashboard_preserves_values():
    """Dashboard should preserve supplied values."""

    equity = [10000.0, 10200.0]

    portfolio = {
        "net_profit": 200.0,
        "total_trades": 2,
    }

    drawdown = {
        "max_drawdown": 50.0,
    }

    streaks = {
        "longest_win_streak": 2,
    }

    distribution = {
        "largest_win": 120.0,
    }

    report = "Professional Report"

    dashboard = PortfolioDashboard.build(
        equity_curve=equity,
        portfolio_stats=portfolio,
        drawdown_stats=drawdown,
        streak_stats=streaks,
        distribution_stats=distribution,
        report=report,
    )

    assert dashboard["equity_curve"] == equity
    assert dashboard["portfolio"] == portfolio
    assert dashboard["drawdown"] == drawdown
    assert dashboard["streaks"] == streaks
    assert dashboard["distribution"] == distribution
    assert dashboard["report"] == report
