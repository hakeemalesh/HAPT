"""
Tests for the HAPT Professional Portfolio Report.
"""

from app.portfolio.correlation_analysis import CorrelationPair
from app.portfolio.portfolio import (
    Portfolio,
    StrategyAllocation,
)
from app.portfolio.portfolio_report import PortfolioReport
from app.portfolio.rebalancer import RebalanceRecommendation
from app.portfolio.risk_engine import (
    PortfolioRiskEngine,
)


def make_portfolio():
    portfolio = Portfolio(
        name="Professional Portfolio",
        initial_capital=10000.0,
    )

    portfolio.add_strategy(
        StrategyAllocation(
            strategy_name="EMA",
            instrument="MES",
            timeframe="5m",
            capital_allocation=2500.0,
            risk_allocation=20.0,
        )
    )

    portfolio.add_strategy(
        StrategyAllocation(
            strategy_name="VWAP",
            instrument="MNQ",
            timeframe="5m",
            capital_allocation=3500.0,
            risk_allocation=30.0,
        )
    )

    return portfolio


def make_correlations():
    return [
        CorrelationPair(
            "EMA",
            "VWAP",
            0.85,
        )
    ]


def make_recommendations():
    return [
        RebalanceRecommendation(
            strategy_name="EMA",
            current_capital=2500.0,
            target_capital=3000.0,
            adjustment=500.0,
            action="INCREASE",
        )
    ]


def test_generate_report():
    portfolio = make_portfolio()

    report = PortfolioReport.generate(
        portfolio=portfolio,
        risk_summary=PortfolioRiskEngine.summarize(
            portfolio
        ),
        correlations=make_correlations(),
        recommendations=make_recommendations(),
    )

    assert report["portfolio_name"] == (
        "Professional Portfolio"
    )

    assert report["strategy_count"] == 2

    assert report["allocated_capital"] == 6000.0

    assert report["available_capital"] == 4000.0


def test_risk_fields():
    portfolio = make_portfolio()

    report = PortfolioReport.generate(
        portfolio=portfolio,
        risk_summary=PortfolioRiskEngine.summarize(
            portfolio
        ),
        correlations=make_correlations(),
        recommendations=[],
    )

    assert report["total_risk"] == 50.0
    assert report["remaining_risk"] == 50.0
    assert report["within_limits"] is True


def test_correlation_summary():
    portfolio = make_portfolio()

    report = PortfolioReport.generate(
        portfolio=portfolio,
        risk_summary=PortfolioRiskEngine.summarize(
            portfolio
        ),
        correlations=make_correlations(),
        recommendations=[],
    )

    assert report["correlation_pairs"] == 1
    assert report["high_correlations"] == 1


def test_recommendation_summary():
    portfolio = make_portfolio()

    report = PortfolioReport.generate(
        portfolio=portfolio,
        risk_summary=PortfolioRiskEngine.summarize(
            portfolio
        ),
        correlations=[],
        recommendations=make_recommendations(),
    )

    assert (
        report["rebalance_recommendations"]
        == 1
    )

    assert (
        "recommendation"
        in report["recommendation_summary"].lower()
    )


def test_generated_timestamp():
    portfolio = make_portfolio()

    report = PortfolioReport.generate(
        portfolio=portfolio,
        risk_summary=PortfolioRiskEngine.summarize(
            portfolio
        ),
        correlations=[],
        recommendations=[],
    )

    assert report["generated_at"] is not None


def test_summary_exists():
    portfolio = make_portfolio()

    report = PortfolioReport.generate(
        portfolio=portfolio,
        risk_summary=PortfolioRiskEngine.summarize(
            portfolio
        ),
        correlations=[],
        recommendations=[],
    )

    assert "Portfolio" in report["summary"]
