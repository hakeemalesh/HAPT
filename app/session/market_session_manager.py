"""
HAPT Market Session Manager
---------------------------

Determines the current trading session from a selected
market profile.
"""

from datetime import datetime
from zoneinfo import ZoneInfo

from session.market_profiles import MARKET_PROFILES


class MarketSessionManager:
    """Determines the current trading session."""

    def __init__(self, market="CME_FUTURES"):
        """Initialize the selected market profile."""

        self.market = market
        self.profile = MARKET_PROFILES[self.market]

    def get_market_name(self):
        """Return the market name."""

        return self.profile["name"]

    def get_current_time(self):
        """Return the current time in the market timezone."""

        timezone = ZoneInfo(self.profile["timezone"])

        return datetime.now(timezone).time()

    def get_current_session(self):
        """Return the current market session."""

        current_time = self.get_current_time()

        for session in self.profile["sessions"]:

            if session["start"] <= current_time < session["end"]:
                return session

        return {
            "name": "Market Closed",
            "score": 0
        }

    def is_market_open(self):
        """Return True if the market is open."""

        return self.get_current_session()["score"] > 0

    def get_market_context(self):
        """Return all current market information."""

        session = self.get_current_session()

        return {
            "market": self.profile["name"],
            "timezone": self.profile["timezone"],
            "current_time": self.get_current_time().strftime("%H:%M:%S"),
            "session": session["name"],
            "session_score": session["score"],
            "market_open": self.is_market_open()
        }