"""
Tests for the HAPT Portfolio Model.
"""

from app.portfolio.portfolio import (
    Portfolio,
    StrategyAllocation,
)


def make_strategy(
    name="EMA Strategy",
    capital=2500.0,
    risk=30.0,
):
    return StrategyAllocation(
        strategy_name=name,
        instrument="MES",
        timeframe="5m",
        capital_allocation=capital,
        risk_allocation=risk,
    )


def test_portfolio_creation():
    """Portfolio should initialize correctly."""

    portfolio = Portfolio(
        name="Primary Portfolio",
        initial_capital=10000.0,
    )

    assert portfolio.name == "Primary Portfolio"
    assert portfolio.initial_capital == 10000.0
    assert portfolio.strategy_count == 0


def test_add_strategy():
    """Adding a strategy should increase the count."""

    portfolio = Portfolio(
        name="Portfolio",
        initial_capital=10000.0,
    )

    portfolio.add_strategy(make_strategy())

    assert portfolio.strategy_count == 1


def test_allocated_capital():
    """Allocated capital should equal the sum of allocations."""

    portfolio = Portfolio(
        name="Portfolio",
        initial_capital=10000.0,
    )

    portfolio.add_strategy(make_strategy(capital=2500.0))
    portfolio.add_strategy(make_strategy("Breakout", 1500.0, 20.0))

    assert portfolio.allocated_capital == 4000.0


def test_available_capital():
    """Available capital should be initial minus allocated."""

    portfolio = Portfolio(
        name="Portfolio",
        initial_capital=10000.0,
    )

    portfolio.add_strategy(make_strategy(capital=4000.0))

    assert portfolio.available_capital == 6000.0


def test_total_risk():
    """Total risk should equal the sum of strategy risks."""

    portfolio = Portfolio(
        name="Portfolio",
        initial_capital=10000.0,
    )

    portfolio.add_strategy(make_strategy(risk=25.0))
    portfolio.add_strategy(make_strategy("Breakout", 2500.0, 35.0))

    assert portfolio.total_risk == 60.0


def test_created_at():
    """Portfolio should have a UTC timestamp."""

    portfolio = Portfolio(
        name="Portfolio",
        initial_capital=10000.0,
    )

    assert portfolio.created_at is not None
    assert portfolio.created_at.tzinfo is not None


def test_multiple_strategies():
    """Multiple strategies should be tracked correctly."""

    portfolio = Portfolio(
        name="Portfolio",
        initial_capital=20000.0,
    )

    portfolio.add_strategy(make_strategy("EMA", 4000.0, 20.0))
    portfolio.add_strategy(make_strategy("VWAP", 3000.0, 25.0))
    portfolio.add_strategy(make_strategy("ORB", 5000.0, 30.0))

    assert portfolio.strategy_count == 3
    assert portfolio.allocated_capital == 12000.0
    assert portfolio.available_capital == 8000.0
    assert portfolio.total_risk == 75.0
