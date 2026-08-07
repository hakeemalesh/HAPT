"""
HAPT Interactive Brokers Adapter
--------------------------------

Reference Interactive Brokers adapter
using dependency injection.
"""

from abc import ABC, abstractmethod

from app.integration.broker_adapter import BrokerAdapter


class IBClient(ABC):
    """
    Interface implemented by any
    Interactive Brokers client.
    """

    @abstractmethod
    def connect(self) -> bool:
        pass

    @abstractmethod
    def disconnect(self) -> bool:
        pass

    @abstractmethod
    def submit_order(self, order) -> bool:
        pass

    @abstractmethod
    def cancel_order(self, order_id: int) -> bool:
        pass

    @abstractmethod
    def account_balance(self) -> float:
        pass

    @abstractmethod
    def positions(self) -> list[str]:
        pass


class MockIBClient(IBClient):
    """
    Mock Interactive Brokers client used
    for deterministic testing.
    """

    def __init__(self) -> None:
        self.connected = False

    def connect(self) -> bool:
        self.connected = True
        return True

    def disconnect(self) -> bool:
        self.connected = False
        return True

    def submit_order(self, order) -> bool:
        return self.connected

    def cancel_order(self, order_id: int) -> bool:
        return self.connected

    def account_balance(self) -> float:
        return 100000.0

    def positions(self) -> list[str]:
        return []


class InteractiveBrokersAdapter(BrokerAdapter):
    """
    Interactive Brokers adapter.
    """

    def __init__(
        self,
        config,
        credentials,
        client: IBClient,
    ) -> None:
        super().__init__(config, credentials)
        self.client = client

    def connect(self) -> bool:
        if not super().connect():
            return False

        return self.client.connect()

    def disconnect(self) -> bool:
        self.client.disconnect()
        return super().disconnect()

    def submit_order(
        self,
        order,
    ) -> bool:
        return self.client.submit_order(order)

    def cancel_order(
        self,
        order_id: int,
    ) -> bool:
        return self.client.cancel_order(order_id)

    def account_balance(self) -> float:
        return self.client.account_balance()

    def positions(self) -> list[str]:
        return self.client.positions()
