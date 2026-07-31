"""
HAPT Trade Display
------------------

Displays trade information in a professional format.
"""

from app.core.logger import setup_logger
from app.models.trade import Trade


class TradeDisplay:
    """Displays trading information."""

    def __init__(self) -> None:
        """Initialize the trade display."""

        self.logger = setup_logger()

    def show(self, trade: Trade) -> None:
        """
        Display a completed trade setup.
        """

        if not isinstance(trade, Trade):
            raise TypeError(
                "trade must be a Trade instance."
            )

        print()
        print("=" * 40)
        print("           HAPT TRADE SETUP")
        print("=" * 40)

        print(f"Symbol         : {trade.symbol}")
        print(f"Market         : {trade.market}")
        print(f"Signal         : {trade.signal}")
        print(f"Status         : {trade.status}")
        print(f"Grade          : {trade.grade}")

        print("-" * 40)

        print(f"Entry Price    : {trade.entry_price}")
        print(f"Stop Loss      : {trade.stop_loss}")
        print(f"Target Price   : {trade.target_price}")

        print("-" * 40)

        print(f"Position Size  : {trade.position_size}")
        print(f"Risk Amount    : {trade.risk_amount}")
        print(f"Risk/Reward    : {trade.risk_reward}")

        print("-" * 40)

        print(f"Approved       : {trade.approved}")

        ai_decision = getattr(
            trade,
            "ai_decision",
            None,
        )

        ai_confidence = getattr(
            trade,
            "ai_confidence",
            None,
        )

        ai_reason = getattr(
            trade,
            "ai_reason",
            None,
        )

        if ai_decision is not None:
            print(f"AI Decision    : {ai_decision}")

        if ai_confidence is not None:
            print(f"AI Confidence  : {ai_confidence}%")

        if ai_reason:
            print(f"AI Reason      : {ai_reason}")

        if trade.notes:
            print("-" * 40)
            print("Notes:")

            for note in trade.notes:
                print(f" • {note}")

        print("=" * 40)

        self.logger.info(
            "Displayed trade setup for %s.",
            trade.symbol,
        )