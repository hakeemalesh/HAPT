"""
HAPT Yahoo Historical Data
--------------------------

Downloads historical OHLCV candle data from Yahoo Finance
and converts it into HAPT's internal candle format.

Internal Candle Format
----------------------
Each candle returned by this module has the form:

{
    "timestamp": str,
    "open": float,
    "high": float,
    "low": float,
    "close": float,
    "volume": float
}
"""

import yfinance as yf


class YahooHistoricalData:
    """
    Provides historical market data from Yahoo Finance.
    """

    DEFAULT_PERIOD = "5d"
    DEFAULT_INTERVAL = "5m"

    def __init__(
        self,
        period=DEFAULT_PERIOD,
        interval=DEFAULT_INTERVAL,
    ):
        """
        Initialize Yahoo historical data provider.
        """

        self.period = period
        self.interval = interval

    def get_candles(
        self,
        symbol,
        period=None,
        interval=None,
    ):
        """
        Download historical candles.

        Parameters
        ----------
        symbol : str
            Yahoo Finance symbol.

        period : str, optional
            Yahoo Finance history period.

        interval : str, optional
            Yahoo Finance interval.

        Returns
        -------
        list
            List of HAPT candle dictionaries.
        """

        period = period or self.period
        interval = interval or self.interval

        try:

            ticker = yf.Ticker(symbol)

            history = ticker.history(
                period=period,
                interval=interval,
                auto_adjust=False,
            )

            if history.empty:
                return []

            candles = []

            for timestamp, row in history.iterrows():

                candles.append(
                    {
                        "timestamp": str(timestamp),
                        "open": float(row["Open"]),
                        "high": float(row["High"]),
                        "low": float(row["Low"]),
                        "close": float(row["Close"]),
                        "volume": float(row["Volume"]),
                    }
                )

            return candles

        except Exception:

            #
            # Production systems should log this.
            # For now we safely return no candles.
            #
            return []
