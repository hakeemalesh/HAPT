"""
Tests for the HAPT Broker Adapter Base.
"""

from app.integration.broker_adapter import BrokerAdapter
from app.integration.broker_config import BrokerConfig
from app.integration.credentials_manager import Credentials


class DummyBroker(BrokerAdapter):
    """
    Minimal concrete implementation for testing.
    """

    def submit_order(self, order) -> bool:
        return self.connected

    def cancel_order(self, order_id: int) -> bool:
        return self.connected

    def account_balance(self) -> float:
        return 100000.0

    def positions(self) -> list[str]:
        return []


def complete_credentials():
    return Credentials(
        username="user",
        password="pass",
        api_key="key",
        api_secret="secret",
    )


def incomplete_credentials():
    return Credentials()


def test_initialization():
    config = BrokerConfig()

    broker = DummyBroker(
        config=config,
        credentials=complete_credentials(),
    )

    assert broker.config is config
    assert broker.connected is False


def test_connect_success():
    broker = DummyBroker(
        config=BrokerConfig(),
        credentials=complete_credentials(),
    )

    assert broker.connect() is True
    assert broker.connected is True


def test_connect_failure():
    broker = DummyBroker(
        config=BrokerConfig(),
        credentials=incomplete_credentials(),
    )

    assert broker.connect() is False
    assert broker.connected is False


def test_disconnect():
    broker = DummyBroker(
        config=BrokerConfig(),
        credentials=complete_credentials(),
    )

    broker.connect()

    assert broker.disconnect() is True
    assert broker.connected is False


def test_account_balance():
    broker = DummyBroker(
        config=BrokerConfig(),
        credentials=complete_credentials(),
    )

    assert broker.account_balance() == 100000.0


def test_positions():
    broker = DummyBroker(
        config=BrokerConfig(),
        credentials=complete_credentials(),
    )

    assert broker.positions() == []


def test_submit_order_connected():
    broker = DummyBroker(
        config=BrokerConfig(),
        credentials=complete_credentials(),
    )

    broker.connect()

    assert broker.submit_order(None) is True


def test_submit_order_disconnected():
    broker = DummyBroker(
        config=BrokerConfig(),
        credentials=complete_credentials(),
    )

    assert broker.submit_order(None) is False
