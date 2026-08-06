"""
HAPT Futures Tick Value Engine
------------------------------

Provides tick sizes and dollar values for supported
futures contracts.

Used by:

- Profit & Loss Engine
- Position Sizing
- Risk Manager
- Backtesting
- Live Trading
"""


class TickValueEngine:
    """Provides futures tick information."""

    CONTRACTS = {
        "MES": {
            "tick_size": 0.25,
            "tick_value": 1.25,
        },
        "ES": {
            "tick_size": 0.25,
            "tick_value": 12.50,
        },
        "MNQ": {
            "tick_size": 0.25,
            "tick_value": 0.50,
        },
        "NQ": {
            "tick_size": 0.25,
            "tick_value": 5.00,
        },
    }

    @classmethod
    def get_tick_size(
        cls,
        symbol,
    ):
        """
        Return the minimum tick size.
        """

        if symbol not in cls.CONTRACTS:
            raise ValueError(
                f"Unsupported instrument: {symbol}"
            )

        return cls.CONTRACTS[symbol][
            "tick_size"
        ]

    @classmethod
    def get_tick_value(
        cls,
        symbol,
    ):
        """
        Return the dollar value of one tick.
        """

        if symbol not in cls.CONTRACTS:
            raise ValueError(
                f"Unsupported instrument: {symbol}"
            )

        return cls.CONTRACTS[symbol][
            "tick_value"
        ]

    @classmethod
    def calculate_ticks(
        cls,
        symbol,
        entry_price,
        exit_price,
    ):
        """
        Return the number of ticks moved.
        """

        tick_size = cls.get_tick_size(
            symbol
        )

        return (
            exit_price - entry_price
        ) / tick_size
