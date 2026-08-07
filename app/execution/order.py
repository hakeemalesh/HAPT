"""
HAPT Order Model
----------------

Core order models used throughout
the execution subsystem.
"""

from dataclasses import dataclass, field
from datetime import UTC, datetime
from enum import Enum


class OrderSide(str, Enum):
    BUY = "BUY"
    SELL = "SELL"


class OrderType(str, Enum):
    MARKET = "MARKET"
    LIMIT = "LIMIT"
    STOP = "STOP"


class OrderStatus(str, Enum):
    PENDING = "PENDING"
    VALIDATED = "VALIDATED"
    SUBMITTED = "SUBMITTED"
    FILLED = "FILLED"
    CANCELLED = "CANCELLED"
    REJECTED = "REJECTED"


@dataclass(slots=True)
class Order:
    """
    Represents a trading order.
    """

    symbol: str
    side: OrderSide
    order_type: OrderType

    quantity: float

    price: float | None = None

    status: OrderStatus = OrderStatus.PENDING

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )
