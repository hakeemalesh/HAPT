"""
HAPT Trade Display
------------------

Displays trade information in a professional format.
"""

from app.models.trade import Trade


class TradeDisplay:
    """Displays trading information."""

    def show(self, trade: Trade):
        """Display a completed trade setup."""

        print("\n========================================")
        print("           HAPT TRADE SETUP")
        print("========================================")

        print(f"Symbol         : {trade.symbol}")
        print(f"Market         : {trade.market}")
        print(f"Signal         : {trade.signal}")
        print(f"Status         : {trade.status}")
        print(f"Grade          : {trade.grade}")

        print("----------------------------------------")

        print(f"Entry Price    : {trade.entry_price}")
        print(f"Stop Loss      : {trade.stop_loss}")
        print(f"Target Price   : {trade.target_price}")

        print("----------------------------------------")

        print(f"Position Size  : {trade.position_size}")
        print(f"Risk Amount    : {trade.risk_amount}")
        print(f"Risk/Reward    : {trade.risk_reward}")

        print("----------------------------------------")

        print(f"Approved       : {trade.approved}")

        if hasattr(trade, "ai_decision"):
            print(f"AI Decision    : {trade.ai_decision}")

        if hasattr(trade, "ai_confidence"):
            print(f"AI Confidence  : {trade.ai_confidence}%")

        if hasattr(trade, "ai_reason"):
            print(f"AI Reason      : {trade.ai_reason}")

        if trade.notes:
            print("----------------------------------------")
            print("Notes:")
            for note in trade.notes:
                print(f" - {note}")

        print("========================================")