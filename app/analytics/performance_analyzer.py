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

        return sum(
            trade.approved
            for trade in self.journal.get_trades()
        )

    def rejected_trades(self) -> int:
        """Return the number of rejected trades."""

        return (
            self.total_trades()
            - self.approved_trades()
        )

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

        trades = self.journal.get_trades()

        if not trades:
            return 0.0

        total = sum(
            trade.risk_reward
            for trade in trades
        )

        return round(
            total / len(trades),
            2,
        )

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