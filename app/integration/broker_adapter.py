"""
HAPT Broker Adapter Base
------------------------

Base class for all live broker adapters.
"""

from abc import ABC, abstractmethod

from app.execution.broker import Broker
from app.integration.broker_config import BrokerConfig
from app.integration.credentials_manager import Credentials


class BrokerAdapter(Broker, ABC):
    """
    Base implementation shared by all
    live broker adapters.
    """

    def __init__(
        self,
        config: BrokerConfig,
        credentials: Credentials,
    ) -> None:
        self.config = config
        self.credentials = credentials
        self.connected = False

    def connect(self) -> bool:
        """
        Connect to the broker.
        """

        if not self.credentials.is_complete():
            return False

        self.connected = True
        return True

    def disconnect(self) -> bool:
        """
        Disconnect from the broker.
        """

        self.connected = False
        return True

    @abstractmethod
    def submit_order(
        self,
        order,
    ) -> bool:
        """
        Submit an order.
        """

    @abstractmethod
    def cancel_order(
        self,
        order_id: int,
    ) -> bool:
        """
        Cancel an order.
        """

    @abstractmethod
    def account_balance(self) -> float:
        """
        Return account balance.
        """

    @abstractmethod
    def positions(self) -> list[str]:
        """
        Return open positions.
        """
