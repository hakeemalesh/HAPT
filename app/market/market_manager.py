"""
HAPT Market Manager
-------------------

Manages all markets and watchlists used by HAPT.

This module is responsible for:
- Loading watchlists
- Organising symbols
- Returning symbols for scanning
- Preparing for future live market integration
"""


class MarketManager:
    """Manages HAPT watchlists."""

    def __init__(self):
        """Create an empty watchlist."""
        self.symbols = []

    def load_default_watchlist(self):
        """
        Load the permanent HAPT futures watchlist.
        """

        self.symbols = [
            "MES",   # Micro E-mini S&P 500
            "MNQ",   # Micro E-mini Nasdaq
            "M2K",   # Micro Russell 2000
            "MYM",   # Micro Dow Jones
            "ES",    # E-mini S&P 500
            "NQ",    # E-mini Nasdaq
            "RTY",   # Russell 2000
            "YM",    # Dow Jones
            "CL",    # Crude Oil
            "GC",    # Gold
        ]

        print(f"{len(self.symbols)} symbols loaded into HAPT watchlist.")

    def get_symbols(self):
        """Return every symbol in the watchlist."""
        return self.symbols

    def add_symbol(self, symbol):
        """Add a new symbol to the watchlist."""

        if symbol not in self.symbols:
            self.symbols.append(symbol)

    def remove_symbol(self, symbol):
        """Remove a symbol from the watchlist."""

        if symbol in self.symbols:
            self.symbols.remove(symbol)

    def clear_watchlist(self):
        """Remove every symbol."""

        self.symbols.clear()

    def total_symbols(self):
        """Return the number of symbols."""

        return len(self.symbols)