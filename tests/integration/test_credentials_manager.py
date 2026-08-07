"""
Tests for the HAPT Secure Credentials Manager.
"""


from app.integration.credentials_manager import (
    Credentials,
    CredentialsManager,
)


def test_default_credentials():
    credentials = Credentials()

    assert credentials.username == ""
    assert credentials.password == ""
    assert credentials.api_key == ""
    assert credentials.api_secret == ""
    assert credentials.is_complete() is False


def test_complete_credentials():
    credentials = Credentials(
        username="user",
        password="pass",
        api_key="key",
        api_secret="secret",
    )

    assert credentials.is_complete() is True


def test_incomplete_credentials():
    credentials = Credentials(
        username="user",
        password="",
        api_key="key",
        api_secret="secret",
    )

    assert credentials.is_complete() is False


def test_redacted_output():
    credentials = Credentials(
        username="alice",
        password="mypassword",
        api_key="apikey",
        api_secret="secret",
    )

    text = credentials.redacted()

    assert "alice" in text
    assert "mypassword" not in text
    assert "apikey" not in text
    assert "api_secret='***'" in text
    assert "***" in text


def test_load_from_environment(monkeypatch):
    monkeypatch.setenv("HAPT_USERNAME", "demo")
    monkeypatch.setenv("HAPT_PASSWORD", "password")
    monkeypatch.setenv("HAPT_API_KEY", "key")
    monkeypatch.setenv("HAPT_API_SECRET", "secret")

    credentials = CredentialsManager.from_environment()

    assert credentials.username == "demo"
    assert credentials.password == "password"
    assert credentials.api_key == "key"
    assert credentials.api_secret == "secret"


def test_custom_prefix(monkeypatch):
    monkeypatch.setenv("IBKR_USERNAME", "ibuser")
    monkeypatch.setenv("IBKR_PASSWORD", "ibpass")
    monkeypatch.setenv("IBKR_API_KEY", "ibkey")
    monkeypatch.setenv("IBKR_API_SECRET", "ibsecret")

    credentials = CredentialsManager.from_environment(
        prefix="IBKR",
    )

    assert credentials.username == "ibuser"
    assert credentials.password == "ibpass"
    assert credentials.api_key == "ibkey"
    assert credentials.api_secret == "ibsecret"
