"""
Tests for the HAPT Interactive Brokers Adapter.
"""

from app.integration.broker_config import BrokerConfig
from app.integration.credentials_manager import Credentials
from app.integration.interactive_brokers import (
    InteractiveBrokersAdapter,
    MockIBClient,
)


def valid_credentials():
    return Credentials(
        username="user",
        password="pass",
        api_key="key",
        api_secret="secret",
    )


def invalid_credentials():
    return Credentials()


def test_mock_client_connect():
    client = MockIBClient()

    assert client.connect() is True
    assert client.connected is True


def test_adapter_connect_success():
    adapter = InteractiveBrokersAdapter(
        config=BrokerConfig(),
        credentials=valid_credentials(),
        client=MockIBClient(),
    )

    assert adapter.connect() is True
    assert adapter.connected is True


def test_adapter_connect_failure():
    adapter = InteractiveBrokersAdapter(
        config=BrokerConfig(),
        credentials=invalid_credentials(),
        client=MockIBClient(),
    )

    assert adapter.connect() is False
    assert adapter.connected is False


def test_disconnect():
    adapter = InteractiveBrokersAdapter(
        config=BrokerConfig(),
        credentials=valid_credentials(),
        client=MockIBClient(),
    )

    adapter.connect()

    assert adapter.disconnect() is True
    assert adapter.connected is False


def test_submit_order():
    adapter = InteractiveBrokersAdapter(
        config=BrokerConfig(),
        credentials=valid_credentials(),
        client=MockIBClient(),
    )

    adapter.connect()

    assert adapter.submit_order(None) is True


def test_cancel_order():
    adapter = InteractiveBrokersAdapter(
        config=BrokerConfig(),
        credentials=valid_credentials(),
        client=MockIBClient(),
    )

    adapter.connect()

    assert adapter.cancel_order(1) is True


def test_account_balance():
    adapter = InteractiveBrokersAdapter(
        config=BrokerConfig(),
        credentials=valid_credentials(),
        client=MockIBClient(),
    )

    assert adapter.account_balance() == 100000.0


def test_positions():
    adapter = InteractiveBrokersAdapter(
        config=BrokerConfig(),
        credentials=valid_credentials(),
        client=MockIBClient(),
    )

    assert adapter.positions() == []
