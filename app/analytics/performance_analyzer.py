"""
HAPT Performance Analyzer
-------------------------

Analyzes completed trades stored in the Trade Journal.
"""

from collections import Counter

from app.journal.trade_journal import TradeJournal


class PerformanceAnalyzer:
    """Calculates trading performance statistics."""

    def __init__(
        self,
        journal: TradeJournal,
    ):
        """Initialize the analyzer."""

        self.journal = journal

    def total_trades(self) -> int:
        """Return the total number of trades."""

        return self.journal.count()

    def approved_trades(self) -> int:
        """Return the number of approved trades."""

        return self.journal.approved_count()

    def rejected_trades(self) -> int:
        """Return the number of rejected trades."""

        return self.journal.rejected_count()

    def approval_rate(self) -> float:
        """Return approval percentage."""

        return self.journal.approval_rate()

    def average_risk_reward(self) -> float:
        """Return average risk/reward ratio."""

        trades = self.journal.get_trades()

        if not trades:
            return 0.0

        return round(
            sum(
                trade.risk_reward
                for trade in trades
            )
            / len(trades),
            2,
        )

    def grade_distribution(self) -> dict[str, int]:
        """Return trade count by grade."""

        return dict(
            Counter(
                trade.grade
                for trade in self.journal.get_trades()
            )
        )

    def signal_distribution(self) -> dict[str, int]:
        """Return trade count by signal."""

        return dict(
            Counter(
                trade.signal
                for trade in self.journal.get_trades()
            )
        )
