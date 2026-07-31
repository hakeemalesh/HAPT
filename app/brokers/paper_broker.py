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
    ) -> bool:
        """
        Simulate placing a paper trade.

        Returns
        -------
        bool
            True if the simulated order was accepted.
        """

        if not self.connected:
            print("Paper Broker is not connected.")
            return False

        side = side.upper()

        if side not in ("BUY", "SELL"):
            print(f"Invalid order side: {side}")
            return False

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return False

        print(
            f"Paper Trade -> "
            f"{side} {quantity} contract(s) of {symbol}"
        )

        return True