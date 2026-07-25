"""
HAPT Indicator Engine
---------------------

Coordinates all technical indicator calculations.
"""

from app.indicators.ema import EMA
from app.indicators.rsi import RSI
from app.indicators.macd import MACD
from app.indicators.atr import ATR
from app.indicators.vwap import VWAP
from app.indicators.volume import Volume


class IndicatorEngine:
    """Coordinates all technical indicator calculations."""

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
                "average": Volume.average(volumes),

                "relative": Volume.relative(
                    current_volume,
                    volumes
                ),

                "high_volume": Volume.is_high_volume(
                    current_volume,
                    volumes
                ),
            },
        }