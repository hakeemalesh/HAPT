"""
HAPT Market Scanner
-------------------

Scans market symbols and prepares them for analysis.
"""


class MarketScanner:
    """Scans trading symbols for opportunities."""

    def __init__(self):
        self.symbols = []

    def load_symbols(self, symbols):
        """Load symbols into the scanner."""
        self.symbols = symbols

    def scan(self):
        """Scan every loaded symbol."""

        print("Starting market scan...")

        for symbol in self.symbols:
            print(f"Scanning {symbol}...")

        print("Market scan complete.")