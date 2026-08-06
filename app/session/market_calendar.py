"""
HAPT Market Calendar
--------------------

Provides trading calendar information for supported
markets.

Initially supports:

- Weekend detection
- Exchange holiday detection
- Exchange early-close detection

Additional functionality (half-days,
market-specific calendars) will be added in future
nodes.
"""

from datetime import datetime


class MarketCalendar:
    """Provides market calendar utilities."""

    #
    # Exchange holidays.
    #
    HOLIDAYS = {
        (1, 1),      # New Year's Day
        (12, 25),    # Christmas Day
    }

    #
    # Exchange early-close days.
    #
    EARLY_CLOSES = {
        (12, 24),    # Christmas Eve
        (11, 27),    # Black Friday (placeholder)
    }

    def is_weekend(
        self,
        current_time,
    ):
        """
        Return True if the supplied datetime falls on
        Saturday or Sunday.
        """

        if not isinstance(current_time, datetime):
            return False

        return current_time.weekday() >= 5

    def is_holiday(
        self,
        current_time,
    ):
        """
        Return True if the supplied datetime falls on
        a configured exchange holiday.
        """

        if not isinstance(current_time, datetime):
            return False

        return (
            current_time.month,
            current_time.day,
        ) in self.HOLIDAYS

    def is_early_close(
        self,
        current_time,
    ):
        """
        Return True if the supplied datetime falls on
        an exchange early-close day.
        """

        if not isinstance(current_time, datetime):
            return False

        return (
            current_time.month,
            current_time.day,
        ) in self.EARLY_CLOSES

    def is_market_closed(
        self,
        current_time,
    ):
        """
        Return True if the supplied datetime falls on
        a non-trading day.
        """

        return (
            self.is_weekend(current_time)
            or self.is_holiday(current_time)
        )
