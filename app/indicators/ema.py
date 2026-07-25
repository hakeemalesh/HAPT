"""
HAPT Exponential Moving Average (EMA)
-------------------------------------

Calculates Exponential Moving Averages.
"""

from collections.abc import Sequence


class EMA:
    """Calculates Exponential Moving Averages."""

    @staticmethod
    def calculate(prices, period):
        """
        Calculate an EMA.

        Parameters
        ----------
        prices : list or pandas.Series
            Closing prices.
        period : int
            EMA period.

        Returns
        -------
        float | None
            Latest EMA value.
        """

        if period <= 0:
            raise ValueError("period must be greater than 0")

        if prices is None:
            return None

        # Accept lists, tuples and pandas Series
        if not isinstance(prices, Sequence):
            prices = list(prices)

        if len(prices) == 0:
            return None

        if len(prices) == 1:
            return float(prices[0])

        if len(prices) < period:
            return round(sum(prices) / len(prices), 2)

        multiplier = 2 / (period + 1)

        ema = sum(prices[:period]) / period

        for price in prices[period:]:
            ema = ((price - ema) * multiplier) + ema

        return round(float(ema), 2)

    @staticmethod
    def calculate_all(prices):
        """
        Calculate all HAPT EMA values.
        """

        return {
            "ema_9": EMA.calculate(prices, 9),
            "ema_20": EMA.calculate(prices, 20),
            "ema_50": EMA.calculate(prices, 50),
            "ema_200": EMA.calculate(prices, 200),
        }