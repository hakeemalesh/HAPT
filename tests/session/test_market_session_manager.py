"""
Tests for the HAPT Market Session Manager.
"""

from datetime import datetime, time

import pytest

from app.session.market_session_manager import (
    MarketSessionManager,
)


def test_market_name():
    """Market name should be returned."""

    manager = MarketSessionManager()

    assert manager.get_market_name() == "CME Futures"


def test_datetime_input():
    """Injected datetime should be accepted."""

    manager = MarketSessionManager()

    dt = datetime(2026, 7, 1, 10, 0)

    assert manager.get_current_time(dt) == time(10, 0)


def test_time_input():
    """Injected time should be accepted."""

    manager = MarketSessionManager()

    t = time(15, 30)

    assert manager.get_current_time(t) == t


def test_invalid_time_type():
    """Invalid types should raise TypeError."""

    manager = MarketSessionManager()

    with pytest.raises(TypeError):
        manager.get_current_time("10:00")


def test_market_open_session():
    """10:00 should be Market Open."""

    manager = MarketSessionManager()

    session = manager.get_current_session(
        time(10, 0)
    )

    assert session["name"] == "Market Open"
    assert session["score"] == 5


def test_market_closed_session():
    """03:00 should be Market Closed."""

    manager = MarketSessionManager()

    session = manager.get_current_session(
        time(3, 0)
    )

    assert session["name"] == "Market Closed"
    assert session["score"] == 0


def test_market_open_flag():
    """Market should be open during session."""

    manager = MarketSessionManager()

    assert manager.is_market_open(
        time(10, 0)
    ) is True


def test_market_closed_flag():
    """Market should be closed outside sessions."""

    manager = MarketSessionManager()

    assert manager.is_market_open(
        time(3, 0)
    ) is False


def test_market_context_uses_supplied_time():
    """Context should reflect supplied time."""

    manager = MarketSessionManager()

    context = manager.get_market_context(
        time(15, 15)
    )

    assert context["session"] == "Power Hour"
    assert context["market_open"] is True

def test_saturday_is_closed():
    """Saturday should always be closed."""

    manager = MarketSessionManager()

    session = manager.get_current_session(
        datetime(2026, 7, 25, 10, 0)
    )

    assert session["name"] == "Market Closed"
    assert session["score"] == 0


def test_sunday_is_closed():
    """Sunday should always be closed."""

    manager = MarketSessionManager()

    session = manager.get_current_session(
        datetime(2026, 7, 26, 10, 0)
    )

    assert session["name"] == "Market Closed"
    assert session["score"] == 0
def test_christmas_is_closed():
    """Christmas Day should always be closed."""

    manager = MarketSessionManager()

    session = manager.get_current_session(
        datetime(2026, 12, 25, 10, 0)
    )

    assert session["name"] == "Market Closed"
    assert session["score"] == 0


def test_new_year_is_closed():
    """New Year's Day should always be closed."""

    manager = MarketSessionManager()

    session = manager.get_current_session(
        datetime(2026, 1, 1, 10, 0)
    )

    assert session["name"] == "Market Closed"
    assert session["score"] == 0
def test_session_quality():
    """Market Open should have excellent quality."""

    manager = MarketSessionManager()

    context = manager.get_market_context(
        time(10, 0)
    )

    assert context["session_quality"] == "Excellent"


def test_liquidity():
    """Market Open should report high liquidity."""

    manager = MarketSessionManager()

    context = manager.get_market_context(
        time(10, 0)
    )

    assert context["liquidity"] == "High"


def test_trade_confidence():
    """Market Open should report high confidence."""

    manager = MarketSessionManager()

    context = manager.get_market_context(
        time(10, 0)
    )

    assert context["trade_confidence"] == "High"


def test_early_close_flag():
    """Normal trading day should not be an early close."""

    manager = MarketSessionManager()

    context = manager.get_market_context(
        datetime(2026, 7, 1, 10, 0)
    )

    assert context["early_close"] is False
