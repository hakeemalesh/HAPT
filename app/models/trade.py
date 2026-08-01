"""
HAPT Trade Model
----------------

Represents the complete lifecycle of a trade,
from planning through execution and closure.
"""

from dataclasses import dataclass, field
from datetime import datetime
import uuid


@dataclass
class Trade:
    """
    Represents a complete trade throughout
    its lifecycle.
    """

    # ----------------------------------
    # Trade Identity
    # ----------------------------------

    trade_id: str = field(
        default_factory=lambda: str(uuid.uuid4())[:8]
    )

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
    # Planned Prices
    # ----------------------------------

    entry_price: float = 0.0

    stop_loss: float = 0.0

    target_price: float = 0.0

    # ----------------------------------
    # Executed Prices
    # ----------------------------------

    entry_fill_price: float = 0.0

    exit_fill_price: float = 0.0

    # ----------------------------------
    # Position
    # ----------------------------------

    position_size: float = 0.0

    risk_amount: float = 0.0

    risk_reward: float = 0.0

    # ----------------------------------
    # Profit & Loss
    # ----------------------------------

    profit_loss: float = 0.0

    commission: float = 0.0

    slippage: float = 0.0

    # ----------------------------------
    # Trade Timing
    # ----------------------------------

    created_at: datetime = field(
        default_factory=datetime.now
    )

    entry_time: datetime | None = None

    exit_time: datetime | None = None

    # ----------------------------------
    # Status
    # ----------------------------------

    approved: bool = False

    status: str = "PENDING"

    # ----------------------------------
    # Notes
    # ----------------------------------

    notes: list[str] = field(
        default_factory=list
    )