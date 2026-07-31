"""
HAPT Paper Broker
-----------------

Simulates a broker without risking real money.
"""

from app.brokers.base_broker import BaseBroker
from app.core.logger import setup_logger


class PaperBroker(BaseBroker):
    """Paper trading broker implementation."""

    def __init__(self) -> None:
        """Initialize the paper broker."""

        self.connected = False
        self.logger = setup_logger()

    def connect(self) -> None:
        """Connect to the paper broker."""

        self.connected = True

        self.logger.info(
            "Paper Broker connected."
        )

    def disconnect(self) -> None:
        """Disconnect from the paper broker."""

        self.connected = False

        self.logger.info(
            "Paper Broker disconnected."
        )

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

            self.logger.error(
                "Paper Broker is not connected."
            )

            return False

        side = side.upper()

        if side not in ("BUY", "SELL"):

            self.logger.error(
                "Invalid order side: %s",
                side,
            )

            return False

        if quantity <= 0:

            self.logger.error(
                "Quantity must be greater than zero."
            )

            return False

        self.logger.info(
            "Paper Trade -> %s %d contract(s) of %s",
            side,
            quantity,
            symbol,
        )

        return True