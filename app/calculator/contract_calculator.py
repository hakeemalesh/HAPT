"""
HAPT Contract Calculator
------------------------

Performs contract sizing and trade calculations.
"""


class ContractCalculator:
    """Calculates trade risk and reward values."""

    #
    # Dollar value per point
    #
    CONTRACT_VALUES = {
        "MES": 5,
        "MNQ": 2,
        "M2K": 5,
        "MYM": 0.5,
        "ES": 50,
        "NQ": 20,
        "RTY": 50,
        "YM": 5,
        "CL": 1000,
        "GC": 100,
    }

    def get_contract_value(self, symbol):
        """Return the dollar value per point."""

        return self.CONTRACT_VALUES.get(symbol.upper())

    def calculate_risk_amount(
        self,
        stop_distance,
        dollar_per_point,
    ):
        """Calculate dollar risk per contract."""

        return stop_distance * dollar_per_point

    def calculate_position_size(
        self,
        symbol,
        max_risk,
        stop_distance,
    ):
        """Calculate position size."""

        if stop_distance <= 0:
            return 0

        dollar_per_point = self.get_contract_value(symbol)

        if dollar_per_point is None:
            return 0

        risk_per_contract = self.calculate_risk_amount(
            stop_distance,
            dollar_per_point,
        )

        if risk_per_contract <= 0:
            return 0

        return int(
            max_risk // risk_per_contract
        )

    def calculate_take_profit(
        self,
        entry_price,
        stop_distance,
        signal,
        risk_reward=2,
    ):
        """Calculate target price."""

        if signal == "BUY":
            return (
                entry_price
                + stop_distance * risk_reward
            )

        if signal == "SELL":
            return (
                entry_price
                - stop_distance * risk_reward
            )

        return entry_price