"""
HAPT Risk Manager
-----------------

Evaluates whether a proposed trade satisfies
HAPT risk management rules.

Position sizing is intentionally handled by the
PositionSizingEngine.
"""

from app.account.account_manager import AccountManager
from app.models.decision import Decision
from app.models.risk import Risk


class RiskManager:
    """Evaluates trade risk according to HAPT rules."""

    MIN_RISK_REWARD = 2.0
    MIN_APPROVED_GRADE = ("A+", "A")

    def __init__(self, account_manager=None):
        """Initialize the Risk Manager."""

        self.account_manager = (
            account_manager
            if account_manager is not None
            else AccountManager()
        )

    def get_max_risk(self) -> float:
        """Return the maximum dollar risk per trade."""

        return self.account_manager.get_max_trade_risk()

    def evaluate(
        self,
        decision: Decision,
        entry_price: float,
        stop_loss: float,
        target_price: float,
        position_size: float,
    ) -> Risk:
        """
        Evaluate whether a trade satisfies
        HAPT risk management rules.
        """

        risk = Risk()

        max_risk = self.get_max_risk()

        risk.risk_amount = max_risk
        risk.entry_price = entry_price
        risk.stop_loss = stop_loss
        risk.target_price = target_price
        risk.position_size = position_size

        stop_distance = abs(entry_price - stop_loss)
        reward_distance = abs(target_price - entry_price)

        if stop_distance > 0:
            risk.risk_reward = round(
                reward_distance / stop_distance,
                2,
            )
        else:
            risk.risk_reward = 0.0

        #
        # Approval checks
        #

        grade_ok = (
            decision.grade in self.MIN_APPROVED_GRADE
        )

        size_ok = (
            position_size > 0
        )

        reward_ok = (
            risk.risk_reward >= self.MIN_RISK_REWARD
        )

        risk.approved = (
            grade_ok
            and size_ok
            and reward_ok
        )

        #
        # Detailed notes
        #

        if grade_ok:
            risk.notes.append(
                f"Grade {decision.grade} satisfies "
                "minimum quality requirement."
            )
        else:
            risk.notes.append(
                f"Grade {decision.grade} is below "
                f"minimum required grade "
                f"{'/'.join(self.MIN_APPROVED_GRADE)}."
            )

        if size_ok:
            risk.notes.append(
                f"Position size "
                f"({position_size}) is valid."
            )
        else:
            risk.notes.append(
                "Position size must be greater than zero."
            )

        if reward_ok:
            risk.notes.append(
                f"Risk/Reward "
                f"({risk.risk_reward}:1) satisfies "
                "minimum requirement."
            )
        else:
            risk.notes.append(
                f"Risk/Reward "
                f"({risk.risk_reward}:1) is below "
                f"required {self.MIN_RISK_REWARD}:1."
            )

        if risk.approved:
            risk.notes.append(
                "Trade approved by HAPT Risk Manager."
            )
        else:
            risk.notes.append(
                "Trade rejected by HAPT Risk Manager."
            )

        return risk