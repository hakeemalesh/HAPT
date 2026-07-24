"""
HAPT Demo Historical Data
-------------------------

Generates demo OHLCV candles for testing.
"""


class DemoHistoricalData:
    """Creates demo historical candle data."""

    def __init__(self):
        """Initialize demo generator."""

        self.candle_count = 250


    def generate(self, symbol):
        """
        Generate demo candles.

        Returns:
            list of candle dictionaries
        """

        candles = []

        price = 100.0


        for i in range(self.candle_count):

            candle = {

                "timestamp": f"T{i}",

                "open": round(price, 2),

                "high": round(price + 2, 2),

                "low": round(price - 2, 2),

                "close": round(price + 1, 2),

                "volume": 1000 + i * 10
            }


            candles.append(candle)

            price += 0.5


        return candles