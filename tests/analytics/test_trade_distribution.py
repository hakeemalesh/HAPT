"""
Tests for the HAPT Trade Distribution Analysis.
"""

from app.analytics.trade_distribution import TradeDistribution


def test_empty_trade_history():
    """Empty trade history."""

    stats = TradeDistribution.calculate([])

    assert stats["largest_win"] == 0.0
    assert stats["largest_loss"] == 0.0
    assert stats["average_win"] == 0.0
    assert stats["average_loss"] == 0.0
    assert stats["median_win"] == 0.0
    assert stats["median_loss"] == 0.0
    assert stats["win_loss_ratio"] == 0.0
    assert stats["winning_trades"] == 0
    assert stats["losing_trades"] == 0


def test_all_winning_trades():
    """All winning trades."""

    stats = TradeDistribution.calculate(
        [100.0, 300.0, 200.0]
    )

    assert stats["largest_win"] == 300.0
    assert stats["largest_loss"] == 0.0
    assert stats["average_win"] == 200.0
    assert stats["median_win"] == 200.0
    assert stats["winning_trades"] == 3
    assert stats["losing_trades"] == 0


def test_all_losing_trades():
    """All losing trades."""

    stats = TradeDistribution.calculate(
        [-50.0, -100.0, -25.0]
    )

    assert stats["largest_win"] == 0.0
    assert stats["largest_loss"] == -100.0
    assert stats["average_loss"] == 58.33
    assert stats["median_loss"] == -50.0
    assert stats["winning_trades"] == 0
    assert stats["losing_trades"] == 3


def test_mixed_trade_results():
    """Mixed winners and losers."""

    stats = TradeDistribution.calculate(
        [
            200.0,
            -100.0,
            300.0,
            -50.0,
            100.0,
        ]
    )

    assert stats["largest_win"] == 300.0
    assert stats["largest_loss"] == -100.0
    assert stats["average_win"] == 200.0
    assert stats["average_loss"] == 75.0
    assert stats["median_win"] == 200.0
    assert stats["median_loss"] == -75.0
    assert stats["win_loss_ratio"] == 2.67
    assert stats["winning_trades"] == 3
    assert stats["losing_trades"] == 2


def test_break_even_trades_ignored():
    """Break-even trades should not affect distribution."""

    stats = TradeDistribution.calculate(
        [
            100.0,
            0.0,
            -50.0,
            0.0,
            200.0,
        ]
    )

    assert stats["winning_trades"] == 2
    assert stats["losing_trades"] == 1
    assert stats["average_win"] == 150.0
    assert stats["average_loss"] == 50.0
    assert stats["win_loss_ratio"] == 3.0


def test_even_number_of_winners():
    """Median with an even number of winners."""

    stats = TradeDistribution.calculate(
        [
            100.0,
            200.0,
            300.0,
            400.0,
        ]
    )

    assert stats["median_win"] == 250.0


def test_even_number_of_losers():
    """Median with an even number of losers."""

    stats = TradeDistribution.calculate(
        [
            -20.0,
            -40.0,
            -60.0,
            -80.0,
        ]
    )

    assert stats["median_loss"] == -50.0
