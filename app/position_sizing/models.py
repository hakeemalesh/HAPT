"""
HAPT Position Sizing Models
---------------------------

Defines the data structures returned by the
PositionSizingEngine.
"""

from dataclasses import dataclass, field


@dataclass(slots=True)
class PositionSizingResult:
    """
    Stores the result of a position sizing calculation.
    """

    valid: bool
    symbol: str
    asset_type: str
    contracts: int
    risk_per_contract: float
    total_risk: float
    remaining_risk: float
    warnings: list[str] = field(default_factory=list)