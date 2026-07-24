"""
HAPT Indicator Engine
---------------------

Coordinates all technical indicator calculations.
"""

from indicators.ema import EMA
from indicators.rsi import RSI
from indicators.macd import MACD
from indicators.atr import ATR
from indicators.vwap import VWAP
from indicators.volume import Volume


class IndicatorEngine:
    """Coordinates all indicator calculations."""

    @staticmethod
    def calculate(
        closes,
        highs,
        lows,
        volumes
    ):
        """
        Calculate all HAPT indicators.

        Parameters
        ----------
        closes : list
            Closing prices.
        highs : list
            High prices.
        lows : list
            Low prices.
        volumes : list
            Trading volumes.

        Returns
        -------
        dict
            Dictionary containing all indicator values.
        """

        current_volume = volumes[-1] if volumes else 0

        return {

            "ema": EMA.calculate_all(closes),

            "rsi": RSI.calculate(closes),

            "macd": MACD.calculate(closes),

            "atr": ATR.calculate(
                highs,
                lows,
                closes
            ),

            "vwap": VWAP.calculate(
                highs,
                lows,
                closes,
                volumes
            ),

            "volume": {

                "average": Volume.average(
                    volumes
                ),

                "relative": Volume.relative(
                    current_volume,
                    volumes
                ),

                "high_volume": Volume.is_high_volume(
                    current_volume,
                    volumes
                )
            }
        }