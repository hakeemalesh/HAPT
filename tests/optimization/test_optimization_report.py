"""
Tests for the HAPT Professional Optimization Report.
"""

from app.optimization.monte_carlo import MonteCarloResult
from app.optimization.optimization_report import OptimizationReport
from app.optimization.optimization_result import OptimizationResult
from app.optimization.strategy_parameters import StrategyParameters


def make_result():
    params = StrategyParameters(
        instrument="MES",
        timeframe="5m",
        ema_fast=9,
        ema_slow=20,
        atr_period=14,
        atr_multiplier=2.0,
        risk_per_trade=30.0,
    )

    return OptimizationResult(
        parameters=params,
        total_trades=150,
        net_profit=4250.0,
        win_rate=61.5,
        profit_factor=2.15,
        expectancy=28.3,
        max_drawdown=340.0,
    )


def make_monte_carlo():
    return MonteCarloResult(
        simulations=500,
        average_profit=4100.0,
        best_profit=5200.0,
        worst_profit=2950.0,
    )


def test_generate_report():
    report = OptimizationReport.generate(
        best_result=make_result(),
        walk_forward_summary={
            "windows": 5,
            "completed": True,
            "average_net_profit": 4000.0,
            "average_win_rate": 60.0,
        },
        monte_carlo=make_monte_carlo(),
        ranking=1,
    )

    assert report["instrument"] == "MES"
    assert report["timeframe"] == "5m"
    assert report["ranking"] == 1
    assert report["net_profit"] == 4250.0
    assert report["profit_factor"] == 2.15
    assert report["walk_forward"]["completed"] is True
    assert report["monte_carlo"]["simulations"] == 500


def test_summary_contains_key_information():
    report = OptimizationReport.generate(
        best_result=make_result(),
        walk_forward_summary={},
        monte_carlo=make_monte_carlo(),
        ranking=1,
    )

    summary = report["summary"]

    assert "MES" in summary
    assert "5m" in summary
    assert "4250.00" in summary
    assert "2.15" in summary
