"""
Tests for the HAPT Monte Carlo Robustness Engine.
"""

from app.optimization.monte_carlo import (
    MonteCarloEngine,
    MonteCarloResult,
)


def test_empty_trade_list():
    """Empty input should return zero statistics."""

    result = MonteCarloEngine.simulate([])

    assert isinstance(result, MonteCarloResult)
    assert result.simulations == 0
    assert result.average_profit == 0.0
    assert result.best_profit == 0.0
    assert result.worst_profit == 0.0


def test_single_simulation():
    """One simulation should preserve the total profit."""

    trades = [100.0, -50.0, 25.0]

    result = MonteCarloEngine.simulate(
        trades,
        simulations=1,
        seed=42,
    )

    assert result.simulations == 1
    assert result.average_profit == 75.0
    assert result.best_profit == 75.0
    assert result.worst_profit == 75.0


def test_multiple_simulations():
    """Multiple simulations should preserve total P&L."""

    trades = [120.0, -40.0, 60.0, -20.0]

    result = MonteCarloEngine.simulate(
        trades,
        simulations=50,
        seed=123,
    )

    assert result.simulations == 50
    assert result.average_profit == 120.0
    assert result.best_profit == 120.0
    assert result.worst_profit == 120.0


def test_deterministic_seed():
    """Fixed seed should produce repeatable results."""

    trades = [50.0, -10.0, 30.0, -5.0]

    result1 = MonteCarloEngine.simulate(
        trades,
        simulations=25,
        seed=99,
    )

    result2 = MonteCarloEngine.simulate(
        trades,
        simulations=25,
        seed=99,
    )

    assert result1 == result2


def test_result_type():
    """Simulation should return a MonteCarloResult."""

    result = MonteCarloEngine.simulate(
        [10.0, -5.0],
        simulations=5,
        seed=1,
    )

    assert isinstance(result, MonteCarloResult)
