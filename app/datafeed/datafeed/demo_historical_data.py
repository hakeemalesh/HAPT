"""
HAPT Demo Historical Data
-------------------------

Creates sample OHLCV candles for testing.
"""


class DemoHistoricalData:
    """Generates demo historical candles."""

    def generate(self, symbol, candles=250):
        """
        Generate demo candles.

        Parameters
        ----------
        symbol : str
            Trading symbol.

        candles : int
            Number of candles.
        """

        data = []

        price = 100

        for i in range(candles):

            candle = {

                "timestamp": f"T{i}",

                "open": price,

                "high": price + 2,

                "low": price - 1,

                "close": price + 1,

                "volume": 1000 + i

            }

            data.append(candle)

            price += 1


        return data