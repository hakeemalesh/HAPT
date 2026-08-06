"""
HAPT Correlation Analysis
-------------------------

Portfolio correlation utilities.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class CorrelationPair:
    """
    Correlation between two strategies.
    """

    strategy_a: str
    strategy_b: str
    correlation: float


class CorrelationAnalysisEngine:
    """
    Portfolio correlation utilities.
    """

    HIGH_CORRELATION = 0.80

    @staticmethod
    def matrix(
        pairs: list[CorrelationPair],
    ) -> dict[str, dict[str, float]]:
        """
        Build a symmetric correlation matrix.
        """

        matrix: dict[str, dict[str, float]] = {}

        for pair in pairs:

            matrix.setdefault(pair.strategy_a, {})
            matrix.setdefault(pair.strategy_b, {})

            matrix[pair.strategy_a][pair.strategy_a] = 1.0
            matrix[pair.strategy_b][pair.strategy_b] = 1.0

            matrix[pair.strategy_a][pair.strategy_b] = (
                pair.correlation
            )

            matrix[pair.strategy_b][pair.strategy_a] = (
                pair.correlation
            )

        return matrix

    @staticmethod
    def lookup(
        pairs: list[CorrelationPair],
        strategy_a: str,
        strategy_b: str,
    ) -> float | None:
        """
        Look up a pairwise correlation.
        """

        for pair in pairs:

            if (
                pair.strategy_a == strategy_a
                and pair.strategy_b == strategy_b
            ) or (
                pair.strategy_a == strategy_b
                and pair.strategy_b == strategy_a
            ):
                return pair.correlation

        return None

    @staticmethod
    def highly_correlated(
        pairs: list[CorrelationPair],
    ) -> list[CorrelationPair]:
        """
        Return highly correlated pairs.
        """

        return [
            pair
            for pair in pairs
            if abs(pair.correlation)
            >= CorrelationAnalysisEngine.HIGH_CORRELATION
        ]
