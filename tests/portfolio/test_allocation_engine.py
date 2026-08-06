"""
Tests for the HAPT Strategy Allocation Engine.
"""

from app.portfolio.allocation_engine import (
    AllocationResult,
    StrategyAllocationEngine,
)
from app.portfolio.portfolio import (
    Portfolio,
    StrategyAllocation,
)


def make_strategy(
    name="EMA",
    capital=2500.0,
    risk=20.0,
):
    return StrategyAllocation(
        strategy_name=name,
        instrument="MES",
        timeframe="5m",
        capital_allocation=capital,
        risk_allocation=risk,
    )


def test_successful_allocation():
    portfolio = Portfolio(
        name="Portfolio",
        initial_capital=10000.0,
    )

    result = StrategyAllocationEngine.allocate(
        portfolio,
        make_strategy(),
    )

    assert isinstance(result, AllocationResult)
    assert result.success is True
    assert portfolio.strategy_count == 1


def test_duplicate_strategy():
    portfolio = Portfolio(
        name="Portfolio",
        initial_capital=10000.0,
    )

    strategy = make_strategy()

    StrategyAllocationEngine.allocate(
        portfolio,
        strategy,
    )

    result = StrategyAllocationEngine.allocate(
        portfolio,
        strategy,
    )

    assert result.success is False
    assert "Duplicate" in result.message


def test_insufficient_capital():
    portfolio = Portfolio(
        name="Portfolio",
        initial_capital=5000.0,
    )

    strategy = make_strategy(
        capital=6000.0,
    )

    result = StrategyAllocationEngine.allocate(
        portfolio,
        strategy,
    )

    assert result.success is False
    assert "capital" in result.message.lower()


def test_risk_limit_exceeded():
    portfolio = Portfolio(
        name="Portfolio",
        initial_capital=10000.0,
    )

    StrategyAllocationEngine.allocate(
        portfolio,
        make_strategy(
            "Strategy A",
            3000.0,
            60.0,
        ),
    )

    result = StrategyAllocationEngine.allocate(
        portfolio,
        make_strategy(
            "Strategy B",
            3000.0,
            50.0,
        ),
    )

    assert result.success is False
    assert "risk" in result.message.lower()


def test_remaining_capital():
    portfolio = Portfolio(
        name="Portfolio",
        initial_capital=10000.0,
    )

    result = StrategyAllocationEngine.allocate(
        portfolio,
        make_strategy(
            capital=3000.0,
        ),
    )

    assert result.remaining_capital == 7000.0


def test_remaining_risk():
    portfolio = Portfolio(
        name="Portfolio",
        initial_capital=10000.0,
    )

    result = StrategyAllocationEngine.allocate(
        portfolio,
        make_strategy(
            risk=35.0,
        ),
    )

    assert result.remaining_risk == 65.0
