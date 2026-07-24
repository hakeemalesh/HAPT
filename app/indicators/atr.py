"""
HAPT Average True Range (ATR)
-----------------------------

Calculates market volatility using Average True Range.
"""


class ATR:
    """Calculates Average True Range."""

    @staticmethod
    def calculate(highs, lows, closes, period=14):
        """
        Calculate ATR.

        Parameters
        ----------
        highs : list
            High prices.
        lows : list
            Low prices.
        closes : list
            Closing prices.
        period : int
            ATR period.

        Returns
        -------
        float | None
            Latest ATR value.
        """

        if not highs or not lows or not closes:
            return None

        if len(highs) == 1:
            return round(highs[0] - lows[0], 2)

        if len(highs) <= period:
            period = len(highs) - 1

        true_ranges = []

        for i in range(1, len(highs)):
            tr = max(
                highs[i] - lows[i],
                abs(highs[i] - closes[i - 1]),
                abs(lows[i] - closes[i - 1]),
            )

            true_ranges.append(tr)

        if period <= 0:
            return None

        atr = sum(true_ranges[:period]) / period

        return round(atr, 2)