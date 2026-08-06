"""
HAPT Historical Context Builder
-------------------------------

Builds historical market contexts for the
HAPT Backtesting Engine.
"""

from app.pipeline.data_pipeline import DataPipeline


class HistoricalContextBuilder:
    """
    Builds complete historical market contexts
    using the production HAPT DataPipeline.
    """

    def __init__(self):
        """Initialize the builder."""

        self.pipeline = DataPipeline()

    def build(
        self,
        symbol: str,
        price: float,
    ) -> dict | None:
        """
        Build a historical market context.

        Parameters
        ----------
        symbol : str

        price : float

        Returns
        -------
        dict | None
        """

        return self.pipeline.build_context(
            symbol=symbol,
            price=price,
        )
