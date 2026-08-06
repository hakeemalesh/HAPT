"""
Tests for the HAPT Portfolio Rebalancer.
"""

from app.portfolio.portfolio import (
    Portfolio,
    StrategyAllocation,
)
from app.portfolio.rebalancer import (
    PortfolioRebalancer,
    RebalanceRecommendation,
)


def make_strategy(name, capital):
    return StrategyAllocation(
        strategy_name=name,
        instrument="MES",
        timeframe="5m",
        capital_allocation=capital,
        risk_allocation=20.0,
    )


def make_portfolio():
    portfolio = Portfolio(
        name="Portfolio",
        initial_capital=10000.0,
    )

    portfolio.add_strategy(
        make_strategy("EMA", 2500.0)
    )

    portfolio.add_strategy(
        make_strategy("VWAP", 3500.0)
    )

    portfolio.add_strategy(
        make_strategy("ORB", 2000.0)
    )

    return portfolio


def test_increase_recommendation():
    portfolio = make_portfolio()

    recommendations = PortfolioRebalancer.rebalance(
        portfolio,
        {
            "EMA": 3000.0,
        },
    )

    ema = recommendations[0]

    assert isinstance(
        ema,
        RebalanceRecommendation,
    )
    assert ema.action == "INCREASE"
    assert ema.adjustment == 500.0


def test_reduce_recommendation():
    portfolio = make_portfolio()

    recommendations = PortfolioRebalancer.rebalance(
        portfolio,
        {
            "VWAP": 2500.0,
        },
    )

    vwap = recommendations[1]

    assert vwap.action == "REDUCE"
    assert vwap.adjustment == -1000.0


def test_no_change_recommendation():
    portfolio = make_portfolio()

    recommendations = PortfolioRebalancer.rebalance(
        portfolio,
        {
            "ORB": 2000.0,
        },
    )

    orb = recommendations[2]

    assert orb.action == "NONE"
    assert orb.adjustment == 0.0


def test_missing_target_defaults_to_current():
    portfolio = make_portfolio()

    recommendations = PortfolioRebalancer.rebalance(
        portfolio,
        {},
    )

    for recommendation in recommendations:
        assert recommendation.action == "NONE"
        assert recommendation.adjustment == 0.0


def test_multiple_recommendations():
    portfolio = make_portfolio()

    recommendations = PortfolioRebalancer.rebalance(
        portfolio,
        {
            "EMA": 3000.0,
            "VWAP": 2500.0,
            "ORB": 2000.0,
        },
    )

    assert len(recommendations) == 3

    actions = {
        recommendation.strategy_name:
        recommendation.action
        for recommendation in recommendations
    }

    assert actions["EMA"] == "INCREASE"
    assert actions["VWAP"] == "REDUCE"
    assert actions["ORB"] == "NONE"


def test_current_and_target_values():
    portfolio = make_portfolio()

    recommendations = PortfolioRebalancer.rebalance(
        portfolio,
        {
            "EMA": 2800.0,
        },
    )

    ema = recommendations[0]

    assert ema.current_capital == 2500.0
    assert ema.target_capital == 2800.0
    assert ema.adjustment == 300.0
