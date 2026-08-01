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
                "dollar_per_point": 5.00,
                "day_margin": 400.00,
                "max_contracts": 5,
            },

            "MNQ": {
                "name": "Micro E-mini Nasdaq-100",
                "asset_type": "Future",
                "exchange": "CME",
                "tick_size": 0.25,
                "tick_value": 0.50,
                "dollar_per_point": 2.00,
                "day_margin": 500.00,
                "max_contracts": 3,
            },

            "M2K": {
                "name": "Micro E-mini Russell 2000",
                "asset_type": "Future",
                "exchange": "CME",
                "tick_size": 0.10,
                "tick_value": 0.50,
                "dollar_per_point": 5.00,
                "day_margin": 400.00,
                "max_contracts": 5,
            },

            "MYM": {
                "name": "Micro E-mini Dow",
                "asset_type": "Future",
                "exchange": "CBOT",
                "tick_size": 1.00,
                "tick_value": 0.50,
                "dollar_per_point": 0.50,
                "day_margin": 300.00,
                "max_contracts": 5,
            },

            "ES": {
                "name": "E-mini S&P 500",
                "asset_type": "Future",
                "exchange": "CME",
                "tick_size": 0.25,
                "tick_value": 12.50,
                "dollar_per_point": 50.00,
                "day_margin": 2000.00,
                "max_contracts": 1,
            },

            "NQ": {
                "name": "E-mini Nasdaq-100",
                "asset_type": "Future",
                "exchange": "CME",
                "tick_size": 0.25,
                "tick_value": 5.00,
                "dollar_per_point": 20.00,
                "day_margin": 2500.00,
                "max_contracts": 1,
            },

            "RTY": {
                "name": "E-mini Russell 2000",
                "asset_type": "Future",
                "exchange": "CME",
                "tick_size": 0.10,
                "tick_value": 5.00,
                "dollar_per_point": 50.00,
                "day_margin": 2000.00,
                "max_contracts": 1,
            },

            "YM": {
                "name": "E-mini Dow",
                "asset_type": "Future",
                "exchange": "CBOT",
                "tick_size": 1.00,
                "tick_value": 5.00,
                "dollar_per_point": 5.00,
                "day_margin": 1500.00,
                "max_contracts": 1,
            },

            "GC": {
                "name": "Gold Futures",
                "asset_type": "Future",
                "exchange": "COMEX",
                "tick_size": 0.10,
                "tick_value": 10.00,
                "dollar_per_point": 100.00,
                "day_margin": 2000.00,
                "max_contracts": 1,
            },

            "CL": {
                "name": "Crude Oil Futures",
                "asset_type": "Future",
                "exchange": "NYMEX",
                "tick_size": 0.01,
                "tick_value": 10.00,
                "dollar_per_point": 1000.00,
                "day_margin": 2000.00,
                "max_contracts": 1,
            },
        }

    def get_specs(self, symbol):
        """Return specifications for a trading symbol."""

        return self.instruments.get(symbol.upper())

    def is_supported(self, symbol):
        """Return True if the symbol is supported."""

        return symbol.upper() in self.instruments

    def list_symbols(self):
        """Return all supported symbols."""

        return sorted(self.instruments.keys())

    def get_name(self, symbol):
        """Return the instrument name."""

        specs = self.get_specs(symbol)
        return specs.get("name") if specs else None

    def get_exchange(self, symbol):
        """Return the exchange."""

        specs = self.get_specs(symbol)
        return specs.get("exchange") if specs else None

    def get_tick_size(self, symbol):
        """Return the tick size."""

        specs = self.get_specs(symbol)
        return specs.get("tick_size") if specs else None

    def get_tick_value(self, symbol):
        """Return the tick value."""

        specs = self.get_specs(symbol)
        return specs.get("tick_value") if specs else None

    def get_dollar_per_point(self, symbol):
        """Return the dollar value per point."""

        specs = self.get_specs(symbol)
        return specs.get("dollar_per_point") if specs else None

    def get_asset_type(self, symbol):
        """Return the asset type."""

        specs = self.get_specs(symbol)
        return specs.get("asset_type") if specs else None

    def get_day_margin(self, symbol):
        """Return the paper day-trading margin."""

        specs = self.get_specs(symbol)
        return specs.get("day_margin") if specs else None

    def get_max_contracts(self, symbol):
        """Return the maximum permitted contracts."""

        specs = self.get_specs(symbol)
        return specs.get("max_contracts") if specs else None