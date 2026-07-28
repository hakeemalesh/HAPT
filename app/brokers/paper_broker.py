"""
HAPT Paper Broker
-----------------

Simulates a broker without risking real money.
"""

from app.brokers.base_broker import BaseBroker


class PaperBroker(BaseBroker):
    """Paper trading broker implementation."""

    def __init__(self) -> None:
        self.connected = False

    def connect(self) -> None:
        """Connect to the paper broker."""
        self.connected = True
        print("Paper Broker connected.")

    def disconnect(self) -> None:
        """Disconnect from the paper broker."""
        self.connected = False
        print("Paper Broker disconnected.")

    def place_order(
        self,
        symbol: str,
        side: str,
        quantity: int,
    ) -> None:
        """Simulate placing a paper trade."""
        print(
            f"Paper Trade -> {side} {quantity} contract(s) of {symbol}"
        )