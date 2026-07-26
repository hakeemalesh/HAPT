"""
HAPT Risk Model
---------------

Represents the output of the Risk Engine.
"""

from dataclasses import dataclass, field


@dataclass
class Risk:

    approved: bool = False

    risk_amount: float = 0.0

    position_size: float = 0.0

    entry_price: float = 0.0

    stop_loss: float = 0.0

    target_price: float = 0.0

    risk_reward: float = 0.0

    notes: list[str] = field(default_factory=list)