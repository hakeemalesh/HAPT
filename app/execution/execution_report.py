"""
HAPT Professional Execution Report
----------------------------------

Generates professional summaries for
the execution subsystem.
"""

from dataclasses import dataclass, field
from datetime import UTC, datetime

from app.execution.order import OrderStatus
from app.execution.order_manager import ManagedOrder


@dataclass(slots=True)
class ExecutionReport:
    """
    Professional execution report.
    """

    orders: list[ManagedOrder]

    generated_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    @property
    def total_orders(self) -> int:
        return len(self.orders)

    @property
    def filled_orders(self) -> int:
        return sum(
            order.order.status == OrderStatus.FILLED
            for order in self.orders
        )

    @property
    def cancelled_orders(self) -> int:
        return sum(
            order.order.status == OrderStatus.CANCELLED
            for order in self.orders
        )

    @property
    def rejected_orders(self) -> int:
        return sum(
            order.order.status == OrderStatus.REJECTED
            for order in self.orders
        )

    @property
    def pending_orders(self) -> int:
        return sum(
            order.order.status == OrderStatus.PENDING
            for order in self.orders
        )

    @property
    def success_rate(self) -> float:
        if self.total_orders == 0:
            return 0.0

        return (
            self.filled_orders
            / self.total_orders
        ) * 100.0
