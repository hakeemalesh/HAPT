"""
HAPT Data Pipeline
------------------

Coordinates the complete market data flow.
"""

from app.context.market_context import MarketContext
from app.datafeed.market_data import MarketData
from app.indicators.indicator_engine import IndicatorEngine
from app.market_structure.market_structure_analyzer import (
    MarketStructureAnalyzer,
)
from app.opportunity.opportunity_engine import OpportunityEngine
from app.processing.candle_processor import CandleProcessor


class DataPipeline:
    """Coordinates market data processing."""

    def __init__(self):
        """Initialize the pipeline."""

        self.market_data = MarketData()
        self.market_context = MarketContext()
        self.opportunity_engine = OpportunityEngine()

    def build_context(
        self,
        symbol,
        price,
        candles=None,
        current_time=None,
    ):
        """
        Build a complete market context.

        Parameters
        ----------
        symbol : str

        price : float

        candles : list | None

        current_time : datetime | time | None

        Returns
        -------
        dict | None
        """

        #
        # Historical candles
        #
        if candles is None:

            candles = self.market_data.get_historical_data(
                symbol
            )

        if not candles:
            return None

        #
        # Extract OHLCV series
        #
        series = CandleProcessor.extract(
            candles
        )

        if not series:
            return None

        #
        # Technical Indicators
        #
        indicators = IndicatorEngine.calculate(
            closes=series["closes"],
            highs=series["highs"],
            lows=series["lows"],
            volumes=series["volumes"],
        )

        if not indicators:
            return None

        #
        # Market Structure
        #
        structure = (
            MarketStructureAnalyzer.analyze(
                candles
            )
        )

        #
        # Build Context
        #
        market_context = self.market_context.build(
            symbol=symbol,
            price=price,
            indicators=indicators,
            market_structure=structure,
            current_time=current_time,
        )

        #
        # Opportunity Analysis
        #
        market_context["opportunity"] = (
            self.opportunity_engine.score(
                market_context
            )
        )

        return market_context