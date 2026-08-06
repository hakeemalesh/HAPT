"""
HAPT Performance Analyzer
-------------------------

Analyzes completed trades stored in the Trade Journal.
"""

from collections import Counter

from app.journal.trade_journal import TradeJournal


class PerformanceAnalyzer:
    """Calculates trading performance statistics."""

    def __init__(self, journal: TradeJournal):
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

        total = self.total_trades()

        if total == 0:
            return 0.0

        return round(
            (self.approved_trades() / total) * 100,
            2,
        )

    def average_risk_reward(self) -> float:
        """Return average risk/reward ratio."""

        return self.journal.average_risk_reward()

    def grade_distribution(self) -> dict[str, int]:
        """Return trade count by grade."""

        grades = (
            trade.grade
            for trade in self.journal.get_trades()
        )

        return dict(Counter(grades))

    def signal_distribution(self) -> dict[str, int]:
        """Return trade count by signal."""

        signals = (
            trade.signal
            for trade in self.journal.get_trades()
        )

        return dict(Counter(signals))

    def summary(self) -> dict:
        """
        Return a complete performance summary.

        This method is intended for CLI reporting
        and future GUI integration.
        """

        return {
            "total_trades": self.total_trades(),
            "approved_trades": self.approved_trades(),
            "rejected_trades": self.rejected_trades(),
            "approval_rate": self.approval_rate(),
            "average_risk_reward": (
                self.average_risk_reward()
            ),
            "signal_distribution": (
                self.signal_distribution()
            ),
            "grade_distribution": (
                self.grade_distribution()
            ),
        }
