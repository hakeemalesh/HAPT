"""
HAPT Risk Manager
-----------------

Calculates position sizing and validates trade risk.
"""


class RiskManager:
    """Handles all trade risk calculations."""

    def __init__(self):
        self.max_risk = 30.0

    def get_max_risk(self):
        """Return the maximum dollar risk."""
        return self.max_risk

    def calculate_position_size(self, stop_distance, dollar_per_point):
        """Calculate the number of contracts to trade."""

        if stop_distance <= 0:
            return 0

        position_size = self.max_risk / (
            stop_distance * dollar_per_point
        )

        return round(position_size, 2)