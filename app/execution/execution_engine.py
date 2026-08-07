"""
HAPT Execution Engine
---------------------

Simulates execution of validated orders.
"""

from dataclasses import dataclass
from datetime import UTC, datetime

from app.execution.order import OrderStatus
from app.execution.order_manager import ManagedOrder


@dataclass(frozen=True, slots=True)
class ExecutionResult:
    """
    Result of an order execution.
    """

    order_id: int
    executed: bool
    execution_price: float
    executed_at: datetime


class ExecutionEngine:
    """
    Executes managed orders.
    """

    @staticmethod
    def execute(
        managed_order: ManagedOrder,
        execution_price: float,
    ) -> ExecutionResult:
        """
        Execute an order immediately.
        """

        managed_order.order.status = OrderStatus.FILLED

        return ExecutionResult(
            order_id=managed_order.order_id,
            executed=True,
            execution_price=execution_price,
            executed_at=datetime.now(UTC),
        )
