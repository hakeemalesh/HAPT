"""
HAPT Trade Model
----------------

Represents the final trade plan produced
by the Trade Planner.
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Trade:
    """
    Represents a complete trade plan ready for
    journaling or execution.
    """

    symbol: str = ""

    market: str = ""

    signal: str = "WAIT"

    grade: str = "D"

    # ----------------------------------
    # Decision Engine Results
    # ----------------------------------

    score: int = 0

    confidence: float = 0.0

    # ----------------------------------
    # Trade Prices
    # ----------------------------------

    entry_price: float = 0.0

    stop_loss: float = 0.0

    target_price: float = 0.0

    # ----------------------------------
    # Position
    # ----------------------------------

    position_size: float = 0.0

    risk_amount: float = 0.0

    risk_reward: float = 0.0

    # ----------------------------------
    # Status
    # ----------------------------------

    approved: bool = False

    status: str = "PENDING"

    created_at: datetime = field(
        default_factory=datetime.now
    )

    notes: list[str] = field(
        default_factory=list
    )