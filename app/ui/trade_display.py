"""
HAPT Trade Display
------------------

Displays trade information in a professional format.
"""


class TradeDisplay:
    """Displays trading information."""

    def show(self, trade):
        """Display a completed trade setup."""

        print("\n========================================")
        print("        HAPT TRADE SETUP")
        print("========================================")

        print(f"Symbol         : {trade['symbol']}")
        print(f"Signal         : {trade['signal']}")
        print(f"Confidence     : {trade['confidence']}%")

        print("----------------------------------------")

        print(f"Entry Price    : {trade['entry_price']}")
        print(f"Stop Loss      : {trade['stop_loss']}")
        print(f"Take Profit    : {trade['take_profit']}")

        print("----------------------------------------")

        print(f"Risk           : ${trade['risk']}")
        print(f"Position Size  : {trade['position_size']}")
        print(f"Risk/Reward    : {trade['risk_reward']}")

        print("========================================")