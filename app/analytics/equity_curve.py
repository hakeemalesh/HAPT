"""
HAPT Equity Curve Engine
------------------------

Builds an account equity curve from a
sequence of completed trade results.
"""


class EquityCurve:
    """Builds portfolio equity over time."""

    @staticmethod
    def build(
        starting_balance: float,
        trade_results: list[float],
    ) -> list[float]:
        """
        Build the cumulative equity curve.

        Parameters
        ----------
        starting_balance : float

        trade_results : list[float]
            Net P&L for completed trades.

        Returns
        -------
        list[float]
            Equity after every trade.
        """

        equity = [starting_balance]

        balance = starting_balance

        for pnl in trade_results:

            balance += pnl

            equity.append(round(balance, 2))

        return equity
