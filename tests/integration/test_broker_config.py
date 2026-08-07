"""
Tests for the HAPT Broker Configuration Manager.
"""

from app.integration.broker_config import BrokerConfig


def test_default_configuration():
    config = BrokerConfig()

    assert config.broker_name == "paper"
    assert config.host == "localhost"
    assert config.port == 4001
    assert config.paper_trading is True
    assert config.timeout_seconds == 30


def test_custom_configuration():
    config = BrokerConfig(
        broker_name="ibkr",
        host="127.0.0.1",
        port=7497,
        account="DU123456",
        paper_trading=False,
        timeout_seconds=60,
    )

    assert config.broker_name == "ibkr"
    assert config.host == "127.0.0.1"
    assert config.port == 7497
    assert config.account == "DU123456"
    assert config.timeout_seconds == 60


def test_is_live_false_for_paper():
    config = BrokerConfig()

    assert config.is_live is False


def test_is_live_true():
    config = BrokerConfig(
        paper_trading=False,
    )

    assert config.is_live is True


def test_endpoint_property():
    config = BrokerConfig(
        host="192.168.1.100",
        port=5000,
    )

    assert config.endpoint == "192.168.1.100:5000"


def test_timeout_configuration():
    config = BrokerConfig(
        timeout_seconds=120,
    )

    assert config.timeout_seconds == 120
