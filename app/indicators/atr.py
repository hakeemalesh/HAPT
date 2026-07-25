"""
HAPT Average True Range (ATR)
-----------------------------

Calculates market volatility using Average True Range.
"""

from collections.abc import Sequence


class ATR:
    """Calculates Average True Range."""

    @staticmethod
    def calculate(highs, lows, closes, period=14):
        """
        Calculate ATR.

        Parameters
        ----------
        highs : list or pandas.Series
            High prices.
        lows : list or pandas.Series
            Low prices.
        closes : list or pandas.Series
            Closing prices.
        period : int
            ATR period.

        Returns
        -------
        float | None
            Latest ATR value.
        """

        if highs is None or lows is None or closes is None:
            return None

        if not isinstance(highs, Sequence):
            highs = list(highs)

        if not isinstance(lows, Sequence):
            lows = list(lows)

        if not isinstance(closes, Sequence):
            closes = list(closes)

        if not (
            len(highs)
            == len(lows)
            == len(closes)
        ):
            return None

        if len(highs) == 0:
            return None

        if period <= 0:
            return None

        if len(highs) == 1:
            return round(highs[0] - lows[0], 2)

        true_ranges = []

        for i in range(1, len(highs)):
            tr = max(
                highs[i] - lows[i],
                abs(highs[i] - closes[i - 1]),
                abs(lows[i] - closes[i - 1]),
            )

            true_ranges.append(tr)

        if not true_ranges:
            return None

        period = min(period, len(true_ranges))

        atr = sum(true_ranges[-period:]) / period

        return round(atr, 2)