"""
HAPT Data Pipeline
------------------

Coordinates the complete market data flow.
"""

from datafeed.market_data import MarketData
from processing.candle_processor import CandleProcessor
from indicators.indicator_engine import IndicatorEngine
from context.market_context import MarketContext


class DataPipeline:
    """Coordinates market data processing."""

    def __init__(self):
        """Initialize the pipeline."""

        self.market_data = MarketData()
        self.market_context = MarketContext()

    def build_context(self, symbol):
        """
        Build a complete market context.

        Parameters
        ----------
        symbol : str

        Returns
        -------
        dict
        """

        candles = self.market_data.get_historical_data(symbol)

        if not candles:
            return None

        series = CandleProcessor.extract(candles)

        indicators = IndicatorEngine.calculate(
            closes=series["closes"],
            highs=series["highs"],
            lows=series["lows"],
            volumes=series["volumes"]
        )

        return self.market_context.build(
            indicators=indicators
        )