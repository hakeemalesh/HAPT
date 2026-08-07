"""
Builds historical market contexts for the
HAPT Backtesting Engine.
"""

from datetime import datetime, time

from app.pipeline.data_pipeline import DataPipeline


class HistoricalContextBuilder:
    """
    Builds complete historical market contexts
    using the production HAPT DataPipeline.
    """

    def __init__(self) -> None:
        """Initialize the builder."""

        self.pipeline: DataPipeline = DataPipeline()

    def build(
        self,
        symbol: str,
        price: float,
        candles: list | None = None,
        current_time: datetime | time | None = None,
    ) -> dict | None:
        """
        Build a historical market context.

        Parameters
        ----------
        symbol : str

        price : float

        candles : list |None
            Historical candles supplied by the replay engine.

        current_time : datetime | time | None
            Historical replay time.

        Returns
        -------
        dict | None
        """

        market_context: dict | None = (
            self.pipeline.build_context(
                symbol=symbol,
                price=price,
                candles=candles,
                current_time=current_time,
            )
        )

        return market_context