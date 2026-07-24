"""
HAPT Trade Setup
================

This module defines the standard TradeSetup object used
throughout the Hybrid AI Trading Platform (HAPT).

Every completed trade setup should be represented by this
class so that every module speaks the same language.

Author:
HAPT Development
"""


class TradeSetup:
    """
    Represents one complete trade setup.
    """

    def __init__(
        self,
        symbol,
        signal,
        confidence,
        grade,
        entry_price,
        stop_loss,
        take_profit,
        position_size,
        risk_reward,
        market_context,
        explanation=""
    ):
        self.symbol = symbol

        self.signal = signal
        self.confidence = confidence
        self.grade = grade

        self.entry_price = entry_price
        self.stop_loss = stop_loss
        self.take_profit = take_profit

        self.position_size = position_size
        self.risk_reward = risk_reward

        self.market_context = market_context

        self.explanation = explanation

    @property
    def risk(self):
        """
        Returns the monetary/price risk
        between entry and stop.
        """

        if (
            self.entry_price is None
            or self.stop_loss is None
        ):
            return None

        return abs(self.entry_price - self.stop_loss)

    def to_dict(self):
        """
        Convert TradeSetup into a dictionary.

        Useful for:
            • Journal
            • JSON export
            • Dashboard
            • AI output
        """

        return {

            "symbol": self.symbol,

            "signal": self.signal,

            "confidence": self.confidence,

            "grade": self.grade,

            "entry_price": self.entry_price,

            "stop_loss": self.stop_loss,

            "take_profit": self.take_profit,

            "position_size": self.position_size,

            "risk_reward": self.risk_reward,

            "risk": self.risk,

            "market_context": self.market_context,

            "explanation": self.explanation
        }

    def __repr__(self):
        """
        Developer-friendly representation.
        """

        return (
            f"TradeSetup("
            f"{self.symbol}, "
            f"{self.signal}, "
            f"{self.confidence}%, "
            f"{self.grade})"
        )