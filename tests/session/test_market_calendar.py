"""
Tests for the HAPT Market Calendar.
"""

from datetime import datetime

from app.session.market_calendar import MarketCalendar


def test_weekday_is_not_weekend():
    """Weekday should not be weekend."""

    calendar = MarketCalendar()

    assert (
        calendar.is_weekend(
            datetime(2026, 7, 22, 10, 0)
        )
        is False
    )


def test_saturday_is_weekend():
    """Saturday should be weekend."""

    calendar = MarketCalendar()

    assert (
        calendar.is_weekend(
            datetime(2026, 7, 25, 10, 0)
        )
        is True
    )


def test_sunday_is_weekend():
    """Sunday should be weekend."""

    calendar = MarketCalendar()

    assert (
        calendar.is_weekend(
            datetime(2026, 7, 26, 10, 0)
        )
        is True
    )


def test_christmas_is_holiday():
    """Christmas should be holiday."""

    calendar = MarketCalendar()

    assert (
        calendar.is_holiday(
            datetime(2026, 12, 25, 10, 0)
        )
        is True
    )


def test_new_year_is_holiday():
    """New Year's Day should be holiday."""

    calendar = MarketCalendar()

    assert (
        calendar.is_holiday(
            datetime(2026, 1, 1, 10, 0)
        )
        is True
    )


def test_normal_day_is_not_holiday():
    """Normal weekday should not be holiday."""

    calendar = MarketCalendar()

    assert (
        calendar.is_holiday(
            datetime(2026, 7, 22, 10, 0)
        )
        is False
    )


def test_christmas_eve_is_early_close():
    """Christmas Eve should be an early-close day."""

    calendar = MarketCalendar()

    assert (
        calendar.is_early_close(
            datetime(2026, 12, 24, 10, 0)
        )
        is True
    )


def test_black_friday_is_early_close():
    """Configured Black Friday should be an early-close day."""

    calendar = MarketCalendar()

    assert (
        calendar.is_early_close(
            datetime(2026, 11, 27, 10, 0)
        )
        is True
    )


def test_normal_day_is_not_early_close():
    """Normal weekday should not be an early-close day."""

    calendar = MarketCalendar()

    assert (
        calendar.is_early_close(
            datetime(2026, 7, 22, 10, 0)
        )
        is False
    )


def test_market_closed_weekend():
    """Weekend should close market."""

    calendar = MarketCalendar()

    assert (
        calendar.is_market_closed(
            datetime(2026, 7, 25, 10, 0)
        )
        is True
    )


def test_market_closed_holiday():
    """Holiday should close market."""

    calendar = MarketCalendar()

    assert (
        calendar.is_market_closed(
            datetime(2026, 12, 25, 10, 0)
        )
        is True
    )


def test_market_open_normal_day():
    """Normal weekday should be tradable."""

    calendar = MarketCalendar()

    assert (
        calendar.is_market_closed(
            datetime(2026, 7, 22, 10, 0)
        )
        is False
    )