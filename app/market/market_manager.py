"""
HAPT Market Manager
-------------------

Responsible for managing all market symbols that HAPT can analyze.
"""


class MarketManager:
    """Manages markets, watchlists and trading symbols."""

    def __init__(self):
        self.symbols = []

    def load_default_watchlist(self):
        """Load the default watchlist."""

        self.symbols = [
            "MES",
            "MNQ",
        ]

    def get_symbols(self):
        """Return the current symbol list."""

        return self.symbols