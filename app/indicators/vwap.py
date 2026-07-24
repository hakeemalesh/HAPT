"""
HAPT Volume Weighted Average Price (VWAP)
-----------------------------------------

Calculates the Volume Weighted Average Price.
"""


class VWAP:
    """Calculates VWAP."""

    @staticmethod
    def calculate(highs, lows, closes, volumes):
        """
        Calculate VWAP.

        Parameters
        ----------
        highs : list
            High prices.
        lows : list
            Low prices.
        closes : list
            Closing prices.
        volumes : list
            Trading volumes.

        Returns
        -------
        float | None
            Latest VWAP value.
        """

        if not (
            len(highs)
            == len(lows)
            == len(closes)
            == len(volumes)
        ):
            return None

        if len(closes) == 0:
            return None

        cumulative_price_volume = 0
        cumulative_volume = 0

        for high, low, close, volume in zip(
            highs,
            lows,
            closes,
            volumes
        ):
            typical_price = (high + low + close) / 3

            cumulative_price_volume += (
                typical_price * volume
            )

            cumulative_volume += volume

        if cumulative_volume == 0:
            return None

        vwap = (
            cumulative_price_volume
            / cumulative_volume
        )

        return round(vwap, 2)