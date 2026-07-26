"""
HAPT Trade Model
----------------

Represents the final trade plan produced
by the Strategy Engine.
"""

from dataclasses import dataclass, field


@dataclass
class Trade:

    symbol: str = ""

    market: str = ""

    signal: str = "WAIT"

    grade: str = "D"

    entry_price: float = 0.0

    stop_loss: float = 0.0

    target_price: float = 0.0

    position_size: float = 0.0

    risk_amount: float = 0.0

    risk_reward: float = 0.0

    approved: bool = False

    notes: list[str] = field(default_factory=list)