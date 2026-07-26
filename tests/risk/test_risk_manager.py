"""
Tests for the HAPT Risk Manager.
"""

from app.models.decision import Decision
from app.risk.risk_manager import RiskManager


def test_position_size():
    """Position size should be calculated correctly."""

    manager = RiskManager()

    size = manager.calculate_position_size(
        stop_distance=5,
        dollar_per_point=5,
    )

    assert size == 1.2


def test_zero_stop_distance():
    """Zero stop distance should return zero."""

    manager = RiskManager()

    size = manager.calculate_position_size(
        stop_distance=0,
        dollar_per_point=5,
    )

    assert size == 0


def test_approved_trade():
    """High-quality trade should be approved."""

    manager = RiskManager()

    decision = Decision()

    decision.grade = "A+"

    risk = manager.evaluate(
        decision=decision,
        entry_price=100,
        stop_loss=95,
        target_price=110,
        dollar_per_point=1,
    )

    assert risk.approved is True

    assert risk.risk_reward == 2.0


def test_rejected_trade():
    """Poor risk/reward trade should be rejected."""

    manager = RiskManager()

    decision = Decision()

    decision.grade = "B"

    risk = manager.evaluate(
        decision=decision,
        entry_price=100,
        stop_loss=95,
        target_price=103,
        dollar_per_point=1,
    )

    assert risk.approved is False