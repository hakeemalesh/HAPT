"""
HAPT Strategy Engine
--------------------

Coordinates the HAPT trading workflow.

Workflow
--------
Market Context
      │
      ▼
Decision Engine
      │
      ▼
Risk Manager
      │
      ▼
Trade Model
"""

from app.calculator.contract_calculator import ContractCalculator
from app.decision.decision_engine import DecisionEngine
from app.instruments.instrument_manager import InstrumentManager
from app.models.trade import Trade
from app.risk.risk_manager import RiskManager


class StrategyEngine:
    """Coordinates the complete HAPT trading workflow."""

    DEFAULT_RISK_REWARD = 2.0
    DEFAULT_STOP_DISTANCE = 1.0

    def __init__(self):
        """Initialize engine dependencies."""

        self.decision_engine = DecisionEngine()
        self.risk_manager = RiskManager()
        self.instrument_manager = InstrumentManager()
        self.contract_calculator = ContractCalculator()

    def analyze(
        self,
        context: dict,
        entry_price: float,
    ) -> Trade:
        """
        Analyze a trading opportunity.

        Parameters
        ----------
        context : dict
            Market context.

        entry_price : float
            Current market price.

        Returns
        -------
        Trade
            Completed trade plan.
        """

        decision = self.decision_engine.evaluate(context)

        trade = Trade()

        trade.symbol = decision.symbol
        trade.market = decision.market
        trade.signal = decision.signal
        trade.grade = decision.grade

        #
        # No trade if decision is WAIT
        #
        if decision.signal == "WAIT":

            trade.approved = False
            trade.status = "REJECTED"
            trade.notes = decision.reasons

            return trade

        #
        # Instrument specifications
        #
        specs = self.instrument_manager.get_specs(
            decision.symbol
        )

        if specs:
            dollar_per_point = specs.get(
                "dollar_per_point",
                5.0,
            )
        else:
            dollar_per_point = 5.0

        #
        # Trade prices
        #
        stop_distance = self.DEFAULT_STOP_DISTANCE

        if decision.signal == "BUY":

            stop_loss = (
                entry_price
                - stop_distance
            )

            target_price = (
                self.contract_calculator.calculate_take_profit(
                    entry_price,
                    stop_distance,
                    self.DEFAULT_RISK_REWARD,
                )
            )

        else:

            stop_loss = (
                entry_price
                + stop_distance
            )

            target_price = (
                entry_price
                - (
                    stop_distance
                    * self.DEFAULT_RISK_REWARD
                )
            )

        #
        # Risk Evaluation
        #
        risk = self.risk_manager.evaluate(
            decision=decision,
            entry_price=entry_price,
            stop_loss=stop_loss,
            target_price=target_price,
            dollar_per_point=dollar_per_point,
        )

        #
        # Populate Trade model
        #
        trade.entry_price = risk.entry_price
        trade.stop_loss = risk.stop_loss
        trade.target_price = risk.target_price

        trade.position_size = (
            risk.position_size
        )

        trade.risk_amount = (
            risk.risk_amount
        )

        trade.risk_reward = (
            risk.risk_reward
        )

        trade.approved = (
            risk.approved
        )

        trade.notes.extend(
            decision.reasons
        )

        trade.notes.extend(
            risk.notes
        )

        if risk.approved:
            trade.status = "APPROVED"
        else:
            trade.status = "REJECTED"

        return trade