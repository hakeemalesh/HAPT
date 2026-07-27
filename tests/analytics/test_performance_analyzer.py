"""
Tests for HAPT Performance Analyzer.
"""

from app.analytics.performance_analyzer import (
    PerformanceAnalyzer,
)
from app.journal.trade_journal import TradeJournal
from app.models.trade import Trade


def create_trade(
    approved=True,
    grade="A",
    signal="BUY",
    risk_reward=2.0,
):
    """Create a sample Trade."""

    trade = Trade()

    trade.approved = approved
    trade.grade = grade
    trade.signal = signal
    trade.risk_reward = risk_reward

    return trade


def test_empty_journal():
    """Statistics should be zero for an empty journal."""

    journal = TradeJournal()

    analyzer = PerformanceAnalyzer(journal)

    assert analyzer.total_trades() == 0
    assert analyzer.approved_trades() == 0
    assert analyzer.rejected_trades() == 0
    assert analyzer.approval_rate() == 0.0
    assert analyzer.average_risk_reward() == 0.0
    assert analyzer.grade_distribution() == {}
    assert analyzer.signal_distribution() == {}


def test_total_trades():
    """Total trades should equal journal count."""

    journal = TradeJournal()

    journal.add_trade(create_trade())
    journal.add_trade(create_trade())

    analyzer = PerformanceAnalyzer(journal)

    assert analyzer.total_trades() == 2


def test_approved_rejected_counts():
    """Approved and rejected trades should be counted correctly."""

    journal = TradeJournal()

    journal.add_trade(create_trade(True))
    journal.add_trade(create_trade(True))
    journal.add_trade(create_trade(False))

    analyzer = PerformanceAnalyzer(journal)

    assert analyzer.approved_trades() == 2
    assert analyzer.rejected_trades() == 1


def test_approval_rate():
    """Approval percentage should be calculated correctly."""

    journal = TradeJournal()

    journal.add_trade(create_trade(True))
    journal.add_trade(create_trade(True))
    journal.add_trade(create_trade(False))
    journal.add_trade(create_trade(False))

    analyzer = PerformanceAnalyzer(journal)

    assert analyzer.approval_rate() == 50.0


def test_average_risk_reward():
    """Average risk reward should be calculated."""

    journal = TradeJournal()

    journal.add_trade(create_trade(risk_reward=2.0))
    journal.add_trade(create_trade(risk_reward=3.0))
    journal.add_trade(create_trade(risk_reward=1.0))

    analyzer = PerformanceAnalyzer(journal)

    assert analyzer.average_risk_reward() == 2.0


def test_grade_distribution():
    """Grades should be counted correctly."""

    journal = TradeJournal()

    journal.add_trade(create_trade(grade="A+"))
    journal.add_trade(create_trade(grade="A"))
    journal.add_trade(create_trade(grade="A"))
    journal.add_trade(create_trade(grade="B"))

    analyzer = PerformanceAnalyzer(journal)

    assert analyzer.grade_distribution() == {
        "A+": 1,
        "A": 2,
        "B": 1,
    }


def test_signal_distribution():
    """Signals should be counted correctly."""

    journal = TradeJournal()

    journal.add_trade(create_trade(signal="BUY"))
    journal.add_trade(create_trade(signal="BUY"))
    journal.add_trade(create_trade(signal="WATCH"))
    journal.add_trade(create_trade(signal="WAIT"))

    analyzer = PerformanceAnalyzer(journal)

    assert analyzer.signal_distribution() == {
        "BUY": 2,
        "WATCH": 1,
        "WAIT": 1,
    }