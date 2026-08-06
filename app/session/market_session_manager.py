"""
HAPT Market Session Manager
---------------------------

Determines the trading session from a selected
market profile.

Supports both:

• Live trading (system clock)
• Historical replay (supplied evaluation time)
"""

from datetime import datetime, time
from zoneinfo import ZoneInfo
from app.session.market_calendar import MarketCalendar
from app.session.market_profiles import MARKET_PROFILES


class MarketSessionManager:
    """Determines the current trading session."""

    def __init__(self, market="CME_FUTURES"):
        """Initialize the selected market profile."""

        self.market = market
        self.profile = MARKET_PROFILES[self.market]
        self.calendar = MarketCalendar()
    def get_market_name(self):
        """Return the market name."""

        return self.profile["name"]

    def get_current_time(
        self,
        current_time=None,
    ):
        """
        Return the market time.

        If current_time is supplied it is used.
        Otherwise the current system time is used.
        """

        if current_time is not None:

            if isinstance(current_time, datetime):
                return current_time.time()

            if isinstance(current_time, time):
                return current_time

            raise TypeError(
                "current_time must be datetime or time."
            )

        timezone = ZoneInfo(
            self.profile["timezone"]
        )

        return datetime.now(
            timezone
        ).time()

    
    def get_current_session(
        self,
        current_time=None,
    ):
        """Return the current market session."""

        #
        # Historical calendar validation.
        #
        if self.calendar.is_market_closed(current_time):

           return {
               "name": "Market Closed",
               "score": 0,
           }
        market_time = self.get_current_time(
            current_time
        )

        for session in self.profile["sessions"]:

            if (
                session["start"]
                <= market_time
                < session["end"]
            ):
                return session

        return {
            "name": "Market Closed",
            "score": 0,
        }

    def is_market_open(
        self,
        current_time=None,
    ):
        """Return True if market is open."""

        return (
            self.get_current_session(
                current_time
            )["score"] > 0
        )

    def get_market_context(
        self,
        current_time=None,
    ):
        """Return complete market context."""

        market_time = self.get_current_time(
            current_time
        )

        session = self.get_current_session(
            current_time
        )

        return {
            "market": self.profile["name"],
            "timezone": self.profile["timezone"],
            "current_time": market_time.strftime(
                "%H:%M:%S"
            ),
            "session": session["name"],
            "session_score": session["score"],
            "market_open": (
                session["score"] > 0
            ),
        }
