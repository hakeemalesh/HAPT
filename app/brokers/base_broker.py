"""
HAPT Base Broker

Defines the common interface for all broker
implementations.
"""

from abc import ABC, abstractmethod


class BaseBroker(ABC):
    """
    Abstract base class for all broker
    implementations.
    """

    @abstractmethod
    def connect(self) -> None:
        """Connect to the broker."""

    @abstractmethod
    def disconnect(self) -> None:
        """Disconnect from the broker."""

    @abstractmethod
    def place_order(
        self,
        symbol: str,
        side: str,
        quantity: int,
    ) -> bool:
        """
        Place an order through the broker.

        Returns
        -------
        bool
            True if the order is accepted,
            False otherwise.
        """