"""
HAPT Commission Engine
----------------------

Calculates round-trip commissions for supported
futures contracts.

Exchange fees and regulatory fees will be added
in later nodes.
"""


class CommissionEngine:
    """Calculates trade commissions."""

    COMMISSIONS = {
        "MES": 1.24,
        "MNQ": 1.24,
        "ES": 2.48,
        "NQ": 2.48,
    }

    @classmethod
    def calculate(
        cls,
        symbol,
        quantity=1,
    ):
        """
        Calculate total commission.
        """

        if symbol not in cls.COMMISSIONS:
            raise ValueError(
                f"Unsupported instrument: {symbol}"
            )

        commission = (
            cls.COMMISSIONS[symbol]
            * quantity
        )

        #
        # Monetary values are always rounded
        # to two decimal places.
        #
        return round(
            commission,
            2,
        )
