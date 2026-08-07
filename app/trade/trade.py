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


@dataclass
class Trade:
    """Represents one completed or open trade."""

    symbol: str

    direction: str

    quantity: int

    entry_price: float

    entry_time: datetime | None = None

    stop_loss: float | None = None

    take_profit: float | None = None

    exit_price: float | None = None

    exit_time: datetime | None = None

    exit_reason: str | None = None

    gross_pnl: float = 0.0

    commission: float = 0.0

    slippage: float = 0.0

    net_pnl: float = 0.0

    status: str = "OPEN"
