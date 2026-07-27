"""
HAPT Market Scanner
-------------------

Scans market symbols and prepares them for analysis.
"""

from app.instruments.instrument_manager import InstrumentManager


class MarketScanner:
    """Scans trading symbols for opportunities."""

    def __init__(self):
        self.symbols = []
        self.instrument_manager = InstrumentManager()

    def load_symbols(self, symbols):
        """Load symbols into the scanner."""
        self.symbols = symbols

    def validate_symbols(self):
        """
        Return only supported trading symbols.
        """

        valid_symbols = []

        for symbol in self.symbols:
            if self.instrument_manager.is_supported(symbol):
                valid_symbols.append(symbol)

        return valid_symbols

    def scan(self):
        """Scan every loaded symbol."""

        print("Starting market scan...")

        for symbol in self.symbols:
            print(f"Scanning {symbol}...")

        print("Market scan complete.")