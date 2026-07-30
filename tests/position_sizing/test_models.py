"""
Tests for HAPT Position Sizing Models.
"""

from app.position_sizing.models import PositionSizingResult


def test_position_sizing_result_creation():
    """A PositionSizingResult should store its values correctly."""

    result = PositionSizingResult(
        valid=True,
        symbol="MES",
        asset_type="Future",
        contracts=2,
        risk_per_contract=15.0,
        total_risk=30.0,
        remaining_risk=0.0,
        warnings=[]
    )

    assert result.valid is True
    assert result.symbol == "MES"
    assert result.asset_type == "Future"
    assert result.contracts == 2
    assert result.risk_per_contract == 15.0
    assert result.total_risk == 30.0
    assert result.remaining_risk == 0.0
    assert result.warnings == []