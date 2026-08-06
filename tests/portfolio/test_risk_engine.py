"""
Tests for the HAPT Portfolio Risk Engine.
"""

from app.portfolio.portfolio import (
    Portfolio,
    StrategyAllocation,
)
from app.portfolio.risk_engine import (
    PortfolioRiskEngine,
    PortfolioRiskSummary,
)


def make_strategy(
    name,
    capital,
    risk,
):
    return StrategyAllocation(
        strategy_name=name,
        instrument="MES",
        timeframe="5m",
        capital_allocation=capital,
        risk_allocation=risk,
    )


def test_empty_portfolio():
    portfolio = Portfolio(
        name="Portfolio",
        initial_capital=10000.0,
    )

    summary = PortfolioRiskEngine.summarize(
        portfolio
    )

    assert isinstance(summary, PortfolioRiskSummary)
    assert summary.total_risk == 0.0
    assert summary.remaining_risk == 100.0
    assert summary.capital_utilization == 0.0
    assert summary.risk_utilization == 0.0
    assert summary.within_limits is True


def test_single_strategy():
    portfolio = Portfolio(
        name="Portfolio",
        initial_capital=10000.0,
    )

    portfolio.add_strategy(
        make_strategy(
            "EMA",
            2500.0,
            25.0,
        )
    )

    summary = PortfolioRiskEngine.summarize(
        portfolio
    )

    assert summary.total_risk == 25.0
    assert summary.remaining_risk == 75.0
    assert summary.capital_utilization == 25.0
    assert summary.risk_utilization == 25.0


def test_multiple_strategies():
    portfolio = Portfolio(
        name="Portfolio",
        initial_capital=10000.0,
    )

    portfolio.add_strategy(
        make_strategy(
            "EMA",
            2500.0,
            20.0,
        )
    )

    portfolio.add_strategy(
        make_strategy(
            "VWAP",
            3500.0,
            30.0,
        )
    )

    summary = PortfolioRiskEngine.summarize(
        portfolio
    )

    assert summary.total_risk == 50.0
    assert summary.remaining_risk == 50.0
    assert summary.capital_utilization == 60.0
    assert summary.risk_utilization == 50.0


def test_zero_capital():
    portfolio = Portfolio(
        name="Portfolio",
        initial_capital=0.0,
    )

    summary = PortfolioRiskEngine.summarize(
        portfolio
    )

    assert summary.capital_utilization == 0.0


def test_portfolio_within_limits():
    portfolio = Portfolio(
        name="Portfolio",
        initial_capital=10000.0,
    )

    portfolio.add_strategy(
        make_strategy(
            "EMA",
            4000.0,
            80.0,
        )
    )

    summary = PortfolioRiskEngine.summarize(
        portfolio
    )

    assert summary.within_limits is True


def test_portfolio_exceeds_limits():
    portfolio = Portfolio(
        name="Portfolio",
        initial_capital=10000.0,
    )

    portfolio.add_strategy(
        make_strategy(
            "EMA",
            4000.0,
            70.0,
        )
    )

    portfolio.add_strategy(
        make_strategy(
            "VWAP",
            3000.0,
            40.0,
        )
    )

    summary = PortfolioRiskEngine.summarize(
        portfolio
    )

    assert summary.total_risk == 110.0
    assert summary.remaining_risk == -10.0
    assert summary.within_limits is False
