"""
HAPT Volume Weighted Average Price (VWAP)
-----------------------------------------

Calculates the Volume Weighted Average Price.
"""

from collections.abc import Sequence


class VWAP:
    """Calculates VWAP."""

    @staticmethod
    def calculate(highs, lows, closes, volumes):
        """
        Calculate VWAP.

        Parameters
        ----------
        highs : list or pandas.Series
            High prices.
        lows : list or pandas.Series
            Low prices.
        closes : list or pandas.Series
            Closing prices.
        volumes : list or pandas.Series
            Trading volumes.

        Returns
        -------
        float | None
            Latest VWAP value.
        """

        if highs is None or lows is None or closes is None or volumes is None:
            return None

        if not isinstance(highs, Sequence):
            highs = list(highs)

        if not isinstance(lows, Sequence):
            lows = list(lows)

        if not isinstance(closes, Sequence):
            closes = list(closes)

        if not isinstance(volumes, Sequence):
            volumes = list(volumes)

        if not (
            len(highs)
            == len(lows)
            == len(closes)
            == len(volumes)
        ):
            return None

        if len(closes) == 0:
            return None

        cumulative_price_volume = 0.0
        cumulative_volume = 0.0

        for high, low, close, volume in zip(
            highs,
            lows,
            closes,
            volumes,
        ):
            typical_price = (high + low + close) / 3

            cumulative_price_volume += typical_price * volume
            cumulative_volume += volume

        if cumulative_volume == 0:
            return None

        return round(
            cumulative_price_volume / cumulative_volume,
            2,
        )