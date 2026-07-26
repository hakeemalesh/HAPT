"""
HAPT Risk Manager
-----------------

Calculates position sizing and validates trade risk.
"""

from app.models.decision import Decision
from app.models.risk import Risk


class RiskManager:
    """Handles all trade risk calculations."""

    def __init__(self):
        self.max_risk = 30.0

    def get_max_risk(self):
        """Return the maximum dollar risk."""
        return self.max_risk

    def calculate_position_size(
        self,
        stop_distance,
        dollar_per_point,
    ):
        """
        Calculate the number of contracts or shares.
        """

        if stop_distance <= 0:
            return 0

        position_size = self.max_risk / (
            stop_distance * dollar_per_point
        )

        return round(position_size, 2)

    def evaluate(
        self,
        decision: Decision,
        entry_price: float,
        stop_loss: float,
        target_price: float,
        dollar_per_point: float,
    ) -> Risk:
        """
        Evaluate whether a trade satisfies HAPT
        risk management rules.
        """

        risk = Risk()

        risk.risk_amount = self.max_risk

        risk.entry_price = entry_price

        risk.stop_loss = stop_loss

        risk.target_price = target_price

        stop_distance = abs(
            entry_price - stop_loss
        )

        risk.position_size = (
            self.calculate_position_size(
                stop_distance,
                dollar_per_point,
            )
        )

        reward = abs(
            target_price - entry_price
        )

        if stop_distance > 0:

            risk.risk_reward = round(
                reward / stop_distance,
                2,
            )

        if (
            decision.grade in ("A+", "A")
            and risk.risk_reward >= 2.0
            and risk.position_size > 0
        ):

            risk.approved = True

            risk.notes.append(
                "Trade satisfies HAPT risk rules."
            )

        else:

            risk.approved = False

            risk.notes.append(
                "Trade rejected by HAPT risk rules."
            )

        return risk