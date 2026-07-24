"""
HAPT Candle Processor
---------------------

Converts OHLCV candle data into separate price series
for technical indicator calculations.
"""


class CandleProcessor:
    """Processes historical candle data."""

    @staticmethod
    def extract(candles):
        """
        Extract price series from candle data.

        Parameters
        ----------
        candles : list
            List of OHLCV candle dictionaries.

        Returns
        -------
        dict
            Dictionary containing separated price series.
        """

        if not candles:
            return {
                "timestamps": [],
                "opens": [],
                "highs": [],
                "lows": [],
                "closes": [],
                "volumes": [],
            }

        return {

            "timestamps": [
                candle["timestamp"]
                for candle in candles
            ],

            "opens": [
                candle["open"]
                for candle in candles
            ],

            "highs": [
                candle["high"]
                for candle in candles
            ],

            "lows": [
                candle["low"]
                for candle in candles
            ],

            "closes": [
                candle["close"]
                for candle in candles
            ],

            "volumes": [
                candle["volume"]
                for candle in candles
            ],
        }