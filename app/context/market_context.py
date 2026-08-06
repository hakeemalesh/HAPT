"""
HAPT Market Context
-------------------

Creates a single source of truth for the current market.
"""

from app.session.market_session_manager import (
    MarketSessionManager,
)


class MarketContext:
    """Collects information about the current market."""

    def __init__(self, market="CME_FUTURES"):
        """Initialize the market context."""

        self.session_manager = MarketSessionManager(market)

    def build(
        self,
        symbol,
        indicators,
        price,
        market_structure=None,
        current_time=None,
    ):
        """
        Build the current market context.

        Parameters
        ----------
        symbol : str

        indicators : dict

        price : float

        market_structure : dict, optional

        current_time : datetime | time, optional

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

        if price is None:
            raise ValueError(
                "Price cannot be None."
            )

        session = self.session_manager.get_market_context(
            current_time=current_time
        )

        if not session:
            raise ValueError(
                "Market session information unavailable."
            )

        ema = indicators.get("ema", {})
        macd = indicators.get("macd", {})
        volume = indicators.get("volume", {})

        if market_structure is None:

            market_structure = {
                "structure": None,
                "trend": None,
                "strength": 0,
                "higher_highs": False,
                "higher_lows": False,
                "lower_highs": False,
                "lower_lows": False,
            }

        return {

            #
            # Instrument
            #
            "symbol": symbol,
            "price": price,

            #
            # Market Information
            #
            "market": session.get("market"),
            "timezone": session.get("timezone"),
            "current_time": session.get("current_time"),
            "market_open": session.get("market_open"),

            #
            # Session
            #
            "session": session.get("session"),
            "session_score": session.get("session_score"),

            #
            # Indicators
            #
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

            #
            # Market Structure
            #
            "market_structure":
                market_structure.get("structure"),

            "market_trend":
                market_structure.get("trend"),

            "structure_strength":
                market_structure.get("strength"),

            "higher_highs":
                market_structure.get("higher_highs"),

            "higher_lows":
                market_structure.get("higher_lows"),

            "lower_highs":
                market_structure.get("lower_highs"),

            "lower_lows":
                market_structure.get("lower_lows"),

            #
            # Future Expansion
            #
            "economic_news": None,
            "holiday": None,
            "market_regime": None,
        }
