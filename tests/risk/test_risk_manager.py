"""
Tests for the HAPT Risk Manager.
"""

from app.models.decision import Decision
from app.risk.risk_manager import RiskManager


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
        position_size=1.2,
    )

    assert risk.approved is True
    assert risk.position_size == 1.2
    assert risk.risk_reward == 2.0
    assert risk.risk_amount == 30.0
    assert "Trade approved by HAPT Risk Manager." in risk.notes


def test_rejected_trade_due_to_grade():
    """Trades below grade A should be rejected."""

    manager = RiskManager()

    decision = Decision()
    decision.grade = "B"

    risk = manager.evaluate(
        decision=decision,
        entry_price=100,
        stop_loss=95,
        target_price=110,
        position_size=1.2,
    )

    assert risk.approved is False
    assert "Trade rejected by HAPT Risk Manager." in risk.notes


def test_rejected_trade_due_to_risk_reward():
    """Trades with insufficient risk/reward should be rejected."""

    manager = RiskManager()

    decision = Decision()
    decision.grade = "A+"

    risk = manager.evaluate(
        decision=decision,
        entry_price=100,
        stop_loss=95,
        target_price=103,
        position_size=1.2,
    )

    assert risk.approved is False
    assert risk.risk_reward == 0.6


def test_rejected_trade_due_to_zero_position_size():
    """Trades with zero position size should be rejected."""

    manager = RiskManager()

    decision = Decision()
    decision.grade = "A+"

    risk = manager.evaluate(
        decision=decision,
        entry_price=100,
        stop_loss=95,
        target_price=110,
        position_size=0,
    )

    assert risk.approved is False