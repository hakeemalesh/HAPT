"""
HAPT Execution Engine
---------------------

Executes approved trades using the configured broker
and updates the live account state.
"""

from app.account.account_manager import AccountManager
from app.brokers.paper_broker import PaperBroker
from app.models.trade import Trade


class ExecutionEngine:
    """Executes approved HAPT trades."""

    def __init__(
        self,
        broker=None,
        account=None,
    ):
        """Initialize the execution engine."""

        self.broker = broker or PaperBroker()
        self.account = account or AccountManager()

    def execute(
        self,
        trade: Trade,
    ) -> Trade:
        """
        Execute a trade.
        """

        #
        # Reject unapproved trades
        #

        if not trade.approved:

            trade.status = "REJECTED"

            trade.notes.append(
                "Trade was not approved for execution."
            )

            return trade

        #
        # Submit order
        #

        order_success = self.broker.place_order(
            symbol=trade.symbol,
            side=trade.signal,
            quantity=int(trade.position_size),
        )

        if not order_success:

            trade.status = "FAILED"

            trade.approved = False

            trade.notes.append(
                "Broker rejected paper trade."
            )

            return trade

        #
        # Simulate broker fill
        #

        trade = self.broker.fill_trade(trade)

        trade.status = "EXECUTED"

        trade.notes.append(
            "Paper trade executed successfully."
        )

        #
        # Update account state
        #

        state = self.account.get_state()

        state.increment_open_trades()

        return trade

    def close_trade(
        self,
        trade: Trade,
        profit_loss: float,
    ) -> Trade:
        """
        Close a trade and update
        the account statistics.
        """

        state = self.account.get_state()

        state.process_trade(profit_loss)

        trade.profit_loss = profit_loss

        trade.exit_fill_price = trade.entry_fill_price + (
            profit_loss / max(
                trade.position_size,
                1,
            )
        )

        from datetime import datetime

        trade.exit_time = datetime.now()

        trade.status = "CLOSED"

        trade.notes.append(
            f"Trade closed with P/L: ${profit_loss:.2f}"
        )

        return trade