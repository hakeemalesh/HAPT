"""
HAPT Broker Abstraction Layer
-----------------------------

Defines the broker interface and a
reference paper broker implementation.
"""

from abc import ABC, abstractmethod

from app.execution.order_manager import ManagedOrder


class Broker(ABC):
    """
    Abstract broker interface.
    """

    @abstractmethod
    def connect(self) -> bool:
        """Connect to the broker."""

    @abstractmethod
    def disconnect(self) -> bool:
        """Disconnect from the broker."""

    @abstractmethod
    def submit_order(
        self,
        order: ManagedOrder,
    ) -> bool:
        """Submit an order."""

    @abstractmethod
    def cancel_order(
        self,
        order_id: int,
    ) -> bool:
        """Cancel an order."""

    @abstractmethod
    def account_balance(self) -> float:
        """Return account balance."""

    @abstractmethod
    def positions(self) -> list[str]:
        """Return open positions."""


class PaperBroker(Broker):
    """
    Simple in-memory broker used for
    testing and paper trading.
    """

    def __init__(self) -> None:
        self.connected = False
        self._orders: dict[int, ManagedOrder] = {}
        self._balance = 100_000.0

    def connect(self) -> bool:
        self.connected = True
        return True

    def disconnect(self) -> bool:
        self.connected = False
        return True

    def submit_order(
        self,
        order: ManagedOrder,
    ) -> bool:
        if not self.connected:
            return False

        self._orders[order.order_id] = order
        return True

    def cancel_order(
        self,
        order_id: int,
    ) -> bool:
        return self._orders.pop(order_id, None) is not None

    def account_balance(self) -> float:
        return self._balance

    def positions(self) -> list[str]:
        return [
            managed.order.symbol
            for managed in self._orders.values()
        ]
