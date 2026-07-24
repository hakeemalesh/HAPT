"""
HAPT Contract Calculator
------------------------

Performs contract sizing and trade calculations.
"""


class ContractCalculator:
    """Calculates trade risk and reward values."""

    def calculate_risk_amount(self, stop_distance, dollar_per_point):
        """Calculate dollar risk per contract."""

        return stop_distance * dollar_per_point

    def calculate_position_size(
        self,
        max_risk,
        stop_distance,
        dollar_per_point
    ):
        """Calculate the number of contracts."""

        if stop_distance <= 0:
            return 0

        risk_per_contract = self.calculate_risk_amount(
            stop_distance,
            dollar_per_point
        )

        if risk_per_contract <= 0:
            return 0

        return round(max_risk / risk_per_contract, 2)

    def calculate_take_profit(
        self,
        entry_price,
        stop_distance,
        risk_reward=2
    ):
        """Calculate the take-profit price."""

        return entry_price + (stop_distance * risk_reward)