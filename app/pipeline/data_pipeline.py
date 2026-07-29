"""
HAPT Data Pipeline
------------------

Coordinates the complete market data flow.
"""

from app.datafeed.market_data import MarketData
from app.processing.candle_processor import CandleProcessor
from app.indicators.indicator_engine import IndicatorEngine
from app.context.market_context import MarketContext
from app.opportunity.opportunity_engine import OpportunityEngine


class DataPipeline:
    """Coordinates market data processing."""

    def __init__(self):
        """Initialize the pipeline."""

        self.market_data = MarketData()
        self.market_context = MarketContext()
        self.opportunity_engine = OpportunityEngine()

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

        market_context = self.market_context.build(
            symbol=symbol,
            indicators=indicators,
        )

        market_context["opportunity"] = self.opportunity_engine.score(
            market_context
        )

        return market_context