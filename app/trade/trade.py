"""
HAPT Trade Model
----------------

Represents a complete trade throughout its
lifecycle.

This object is shared by:

- Replay Engine
- Backtesting
- Journal
- Analytics
- Live Trading
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Trade:
    """Represents one completed or open trade."""

    symbol: str

    direction: str

    quantity: int

    entry_price: float

    entry_time: Optional[datetime] = None

    stop_loss: Optional[float] = None

    take_profit: Optional[float] = None

    exit_price: Optional[float] = None

    exit_time: Optional[datetime] = None

    exit_reason: Optional[str] = None

    gross_pnl: float = 0.0

    commission: float = 0.0

    slippage: float = 0.0

    net_pnl: float = 0.0

    status: str = "OPEN"
