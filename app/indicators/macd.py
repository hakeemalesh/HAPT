"""
HAPT MACD
---------

Calculates the Moving Average Convergence Divergence.
"""

from indicators.ema import EMA


class MACD:
    """Calculates MACD values."""

    @staticmethod
    def calculate(prices):
        """
        Calculate the MACD line.

        Parameters
        ----------
        prices : list
            List of closing prices.

        Returns
        -------
        dict | None
            MACD values.
        """

        if not prices:
            return None

        if len(prices) == 1:
            return {
                "ema_12": prices[0],
                "ema_26": prices[0],
                "macd": 0.0,
            }

        ema12 = EMA.calculate(prices, 12)
        ema26 = EMA.calculate(prices, 26)

        if ema12 is None or ema26 is None:
            return None

        macd_line = round(ema12 - ema26, 2)

        return {
            "ema_12": ema12,
            "ema_26": ema26,
            "macd": macd_line,
        }