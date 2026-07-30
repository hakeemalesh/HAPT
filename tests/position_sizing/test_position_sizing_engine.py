"""
Tests for the HAPT Position Sizing Engine.
"""

from app.position_sizing.position_sizing_engine import PositionSizingEngine


def test_invalid_symbol():
    """Unsupported symbols should return an invalid result."""

    engine = PositionSizingEngine()

    result = engine.calculate(
        symbol="XYZ",
        account_risk=30.0,
        stop_distance=6.0
    )

    assert result.valid is False
    assert result.contracts == 0


def test_mes_single_contract():
    """MES should size to one contract."""

    engine = PositionSizingEngine()

    result = engine.calculate(
        symbol="MES",
        account_risk=30.0,
        stop_distance=6.0
    )

    assert result.valid is True
    assert result.contracts == 1
    assert result.total_risk == 30.0
    assert result.remaining_risk == 0.0


def test_risk_too_small():
    """Risk too small should prevent trading."""

    engine = PositionSizingEngine()

    result = engine.calculate(
        symbol="MES",
        account_risk=5.0,
        stop_distance=6.0
    )

    assert result.valid is False
    assert result.contracts == 0