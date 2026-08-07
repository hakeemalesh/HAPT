"""
HAPT Monte Carlo Robustness Engine
----------------------------------

Evaluates strategy robustness by repeatedly
randomizing the order of trade outcomes.
"""

import random
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class MonteCarloResult:
    """
    Summary of Monte Carlo simulations.
    """

    simulations: int
    average_profit: float
    best_profit: float
    worst_profit: float


class MonteCarloEngine:
    """Runs Monte Carlo simulations."""

    @staticmethod
    def simulate(
        trade_results: list[float],
        simulations: int = 100,
        seed: int | None = None,
    ) -> MonteCarloResult:
        """
        Perform Monte Carlo simulations.

        Parameters
        ----------
        trade_results
            Individual trade P&L values.

        simulations
            Number of random simulations.

        seed
            Optional random seed for deterministic testing.
        """

        if seed is not None:
            random.seed(seed)

        if not trade_results:
            return MonteCarloResult(
                simulations=0,
                average_profit=0.0,
                best_profit=0.0,
                worst_profit=0.0,
            )

        totals = []

        for _ in range(simulations):
            shuffled = trade_results[:]
            random.shuffle(shuffled)
            totals.append(sum(shuffled))

        return MonteCarloResult(
            simulations=simulations,
            average_profit=round(sum(totals) / len(totals), 2),
            best_profit=round(max(totals), 2),
            worst_profit=round(min(totals), 2),
        )
