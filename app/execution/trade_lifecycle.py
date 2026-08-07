"""
HAPT Trade Lifecycle Manager
----------------------------

Tracks valid order lifecycle transitions
and records an audit trail.
"""

from dataclasses import dataclass
from datetime import UTC, datetime

from app.execution.order import (
    OrderStatus,
)
from app.execution.order_manager import (
    ManagedOrder,
)


@dataclass(frozen=True, slots=True)
class LifecycleEvent:
    """
    Single lifecycle event.
    """

    status: OrderStatus
    timestamp: datetime


class TradeLifecycle:
    """
    Controls order lifecycle transitions.
    """

    _ALLOWED_TRANSITIONS = {
        OrderStatus.PENDING: {
            OrderStatus.VALIDATED,
            OrderStatus.REJECTED,
        },
        OrderStatus.VALIDATED: {
            OrderStatus.SUBMITTED,
            OrderStatus.CANCELLED,
        },
        OrderStatus.SUBMITTED: {
            OrderStatus.FILLED,
            OrderStatus.CANCELLED,
            OrderStatus.REJECTED,
        },
        OrderStatus.FILLED: set(),
        OrderStatus.CANCELLED: set(),
        OrderStatus.REJECTED: set(),
    }

    def __init__(
        self,
        managed_order: ManagedOrder,
    ) -> None:
        self.managed_order = managed_order

        self._history: list[LifecycleEvent] = [
            LifecycleEvent(
                status=managed_order.order.status,
                timestamp=datetime.now(UTC),
            )
        ]

    def transition_to(
        self,
        status: OrderStatus,
    ) -> bool:
        """
        Transition to a new status if valid.
        """

        current = self.managed_order.order.status

        if status not in self._ALLOWED_TRANSITIONS[current]:
            return False

        self.managed_order.order.status = status

        self._history.append(
            LifecycleEvent(
                status=status,
                timestamp=datetime.now(UTC),
            )
        )

        return True

    def current_status(self) -> OrderStatus:
        """
        Current order status.
        """

        return self.managed_order.order.status

    def history(self) -> list[LifecycleEvent]:
        """
        Complete lifecycle history.
        """

        return list(self._history)

    def event_count(self) -> int:
        """
        Number of lifecycle events.
        """

        return len(self._history)
