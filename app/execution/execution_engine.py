"""
HAPT Execution Engine
---------------------

Executes approved trades using the configured broker.
"""

from app.brokers.paper_broker import PaperBroker
from app.models.trade import Trade


class ExecutionEngine:
    """Executes approved HAPT trades."""

    def __init__(self, broker: PaperBroker):
        """
        Initialize the execution engine.

        Parameters
        ----------
        broker : PaperBroker
            Connected broker instance.
        """

        self.broker = broker

    def execute(
        self,
        trade: Trade,
    ) -> Trade:
        """
        Execute a trade.

        Parameters
        ----------
        trade : Trade

        Returns
        -------
        Trade
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

        else:

            trade.status = "FAILED"
            trade.approved = False

            trade.notes.append(
                "Broker rejected paper trade."
            )

        return trade