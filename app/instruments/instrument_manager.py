"""
HAPT Instrument Manager
-----------------------

Stores the specifications for every trading instrument
supported by HAPT.
"""


class InstrumentManager:
    """Provides instrument specifications."""

    def __init__(self):
        """Initialize the instrument database."""

        self.instruments = {

            "MES": {
                "name": "Micro E-mini S&P 500",
                "asset_type": "Future",
                "exchange": "CME",
                "tick_size": 0.25,
                "tick_value": 1.25,
                "dollar_per_point": 5.00
            },

            "MNQ": {
                "name": "Micro E-mini Nasdaq-100",
                "asset_type": "Future",
                "exchange": "CME",
                "tick_size": 0.25,
                "tick_value": 0.50,
                "dollar_per_point": 2.00
            },

            "M2K": {
                "name": "Micro E-mini Russell 2000",
                "asset_type": "Future",
                "exchange": "CME",
                "tick_size": 0.10,
                "tick_value": 0.50,
                "dollar_per_point": 5.00
            },

            "MYM": {
                "name": "Micro E-mini Dow",
                "asset_type": "Future",
                "exchange": "CBOT",
                "tick_size": 1.00,
                "tick_value": 0.50,
                "dollar_per_point": 0.50
            },

            "ES": {
                "name": "E-mini S&P 500",
                "asset_type": "Future",
                "exchange": "CME",
                "tick_size": 0.25,
                "tick_value": 12.50,
                "dollar_per_point": 50.00
            },

            "NQ": {
                "name": "E-mini Nasdaq-100",
                "asset_type": "Future",
                "exchange": "CME",
                "tick_size": 0.25,
                "tick_value": 5.00,
                "dollar_per_point": 20.00
            },

            "GC": {
                "name": "Gold Futures",
                "asset_type": "Future",
                "exchange": "COMEX",
                "tick_size": 0.10,
                "tick_value": 10.00,
                "dollar_per_point": 100.00
            },

            "CL": {
                "name": "Crude Oil Futures",
                "asset_type": "Future",
                "exchange": "NYMEX",
                "tick_size": 0.01,
                "tick_value": 10.00,
                "dollar_per_point": 1000.00
            }
        }

    def get_specs(self, symbol):
        """Return specifications for a trading symbol."""

        return self.instruments.get(symbol.upper())