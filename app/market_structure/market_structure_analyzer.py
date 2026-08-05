"""
HAPT Market Structure Analyzer
------------------------------

Determines the current market structure from
historical OHLC data.

This module identifies:

- Higher Highs
- Higher Lows
- Lower Highs
- Lower Lows
- Trend Direction
- Structure Strength

The output is consumed by the Professional
Opportunity Engine.
"""


class MarketStructureAnalyzer:
    """
    Analyzes market structure using recent candles.
    """

    LOOKBACK = 20

    @staticmethod
    def analyze(candles):
        """
        Analyze recent market structure.

        Parameters
        ----------
        candles : list
            List of OHLCV candle dictionaries.

        Returns
        -------
        dict
        """

        if not candles or len(candles) < 2:
            return MarketStructureAnalyzer._unknown()

        recent = candles[-MarketStructureAnalyzer.LOOKBACK:]

        highs = [
            candle["high"]
            for candle in recent
        ]

        lows = [
            candle["low"]
            for candle in recent
        ]

        higher_highs = all(
            highs[i] >= highs[i - 1]
            for i in range(1, len(highs))
        )

        higher_lows = all(
            lows[i] >= lows[i - 1]
            for i in range(1, len(lows))
        )

        lower_highs = all(
            highs[i] <= highs[i - 1]
            for i in range(1, len(highs))
        )

        lower_lows = all(
            lows[i] <= lows[i - 1]
            for i in range(1, len(lows))
        )

        if higher_highs and higher_lows:

            structure = "Bullish"
            trend = "Uptrend"
            strength = 100

        elif lower_highs and lower_lows:

            structure = "Bearish"
            trend = "Downtrend"
            strength = 100

        else:

            structure = "Sideways"
            trend = "Range"
            strength = 50

        return {

            "structure": structure,

            "trend": trend,

            "higher_highs": higher_highs,

            "higher_lows": higher_lows,

            "lower_highs": lower_highs,

            "lower_lows": lower_lows,

            "strength": strength,
        }

    @staticmethod
    def _unknown():
        """
        Return default structure.
        """

        return {

            "structure": "Unknown",

            "trend": "Unknown",

            "higher_highs": False,

            "higher_lows": False,

            "lower_highs": False,

            "lower_lows": False,

            "strength": 0,
        }
