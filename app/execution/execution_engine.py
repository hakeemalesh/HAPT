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
        """
        Initialize the execution engine.
        """

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
        # Send order to broker
        #
        order_success = self.broker.place_order(
            symbol=trade.symbol,
            side=trade.signal,
            quantity=int(trade.position_size),
        )

        #
        # Update trade status
        #
        if order_success:

            trade.status = "EXECUTED"

            trade.notes.append(
                "Paper trade executed successfully."
            )

            #
            # Update live account state
            #
            state = self.account.get_state()

            state.increment_open_trades()

        else:

            trade.status = "FAILED"

            trade.approved = False

            trade.notes.append(
                "Broker rejected paper trade."
            )

        return trade