"""
HAPT Market Context
-------------------

Creates a single source of truth for the current market.
"""

from app.session.market_session_manager import MarketSessionManager


class MarketContext:
    """Collects information about the current market."""

    def __init__(self, market="CME_FUTURES"):
        """Initialize the market context."""

        self.session_manager = MarketSessionManager(market)

    def build(self, symbol, indicators):
        """
        Build the current market context.

        Parameters
        ----------
        symbol : str

        indicators : dict

        Returns
        -------
        dict
        """

        if not symbol:
            raise ValueError(
                "Symbol cannot be empty."
            )

        if not indicators:
            raise ValueError(
                "Indicators cannot be empty."
            )

        session = self.session_manager.get_market_context()

        if not session:
            raise ValueError(
                "Market session information unavailable."
            )

        ema = indicators.get("ema", {})
        macd = indicators.get("macd", {})
        volume = indicators.get("volume", {})

        return {

            # Instrument
            "symbol": symbol,

            # Market Information
            "market": session.get("market"),
            "timezone": session.get("timezone"),
            "current_time": session.get("current_time"),
            "market_open": session.get("market_open"),

            # Session
            "session": session.get("session"),
            "session_score": session.get("session_score"),

            # Indicators
            "ema_9": ema.get("ema_9"),
            "ema_20": ema.get("ema_20"),
            "ema_50": ema.get("ema_50"),
            "ema_200": ema.get("ema_200"),

            "rsi": indicators.get("rsi"),

            "macd": macd.get("macd"),

            "atr": indicators.get("atr"),

            "vwap": indicators.get("vwap"),

            "volume": volume.get("average"),

            "relative_volume": volume.get("relative"),

            "high_volume": volume.get("high_volume"),

            # Future Expansion
            "economic_news": None,
            "holiday": None,
            "market_regime": None,
        }