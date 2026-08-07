"""
HAPT Order Management System (OMS)
----------------------------------

Stores, tracks, and manages validated
trading orders.
"""

from dataclasses import dataclass
from itertools import count

from app.execution.order import (
    Order,
    OrderStatus,
)


@dataclass(slots=True)
class ManagedOrder:
    """
    Order tracked by the OMS.
    """

    order_id: int
    order: Order


class OrderManager:
    """
    Central Order Management System.
    """

    def __init__(self) -> None:
        self._orders: dict[int, ManagedOrder] = {}
        self._next_order_id = count(1)

    def submit(
        self,
        order: Order,
    ) -> ManagedOrder:
        """
        Register a validated order.
        """

        order_id = next(self._next_order_id)

        managed = ManagedOrder(
            order_id=order_id,
            order=order,
        )

        self._orders[order_id] = managed

        return managed

    def get(
        self,
        order_id: int,
    ) -> ManagedOrder | None:
        """
        Retrieve an order.
        """

        return self._orders.get(order_id)

    def update_status(
        self,
        order_id: int,
        status: OrderStatus,
    ) -> bool:
        """
        Update order status.
        """

        managed = self.get(order_id)

        if managed is None:
            return False

        managed.order.status = status

        return True

    def cancel(
        self,
        order_id: int,
    ) -> bool:
        """
        Cancel an order.
        """

        return self.update_status(
            order_id,
            OrderStatus.CANCELLED,
        )

    def active_orders(
        self,
    ) -> list[ManagedOrder]:
        """
        Return non-terminal orders.
        """

        terminal = {
            OrderStatus.FILLED,
            OrderStatus.CANCELLED,
            OrderStatus.REJECTED,
        }

        return [
            managed
            for managed in self._orders.values()
            if managed.order.status not in terminal
        ]

    def total_orders(self) -> int:
        """
        Total tracked orders.
        """

        return len(self._orders)
