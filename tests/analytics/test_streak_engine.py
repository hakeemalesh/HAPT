"""
Tests for the HAPT Winning & Losing Streak Engine.
"""

from app.analytics.streak_engine import StreakEngine


def test_empty_results():
    """Empty trade history."""

    stats = StreakEngine.calculate([])

    assert stats["longest_win_streak"] == 0
    assert stats["longest_loss_streak"] == 0
    assert stats["current_win_streak"] == 0
    assert stats["current_loss_streak"] == 0


def test_all_wins():
    """All trades are winners."""

    stats = StreakEngine.calculate(
        [100, 50, 25, 10]
    )

    assert stats["longest_win_streak"] == 4
    assert stats["longest_loss_streak"] == 0
    assert stats["current_win_streak"] == 4
    assert stats["current_loss_streak"] == 0


def test_all_losses():
    """All trades are losers."""

    stats = StreakEngine.calculate(
        [-10, -20, -30]
    )

    assert stats["longest_win_streak"] == 0
    assert stats["longest_loss_streak"] == 3
    assert stats["current_win_streak"] == 0
    assert stats["current_loss_streak"] == 3


def test_mixed_results():
    """Mixed wins and losses."""

    stats = StreakEngine.calculate(
        [
            100,
            50,
            -20,
            -10,
            -30,
            40,
            80,
            -15,
        ]
    )

    assert stats["longest_win_streak"] == 2
    assert stats["longest_loss_streak"] == 3
    assert stats["current_win_streak"] == 0
    assert stats["current_loss_streak"] == 1


def test_break_even_resets_streaks():
    """Break-even trades reset both streaks."""

    stats = StreakEngine.calculate(
        [
            100,
            50,
            0,
            -20,
            -10,
        ]
    )

    assert stats["longest_win_streak"] == 2
    assert stats["longest_loss_streak"] == 2
    assert stats["current_win_streak"] == 0
    assert stats["current_loss_streak"] == 2


def test_current_win_streak():
    """Current winning streak."""

    stats = StreakEngine.calculate(
        [
            -10,
            -5,
            25,
            40,
            30,
        ]
    )

    assert stats["longest_win_streak"] == 3
    assert stats["current_win_streak"] == 3
    assert stats["current_loss_streak"] == 0


def test_current_loss_streak():
    """Current losing streak."""

    stats = StreakEngine.calculate(
        [
            25,
            15,
            -5,
            -10,
            -15,
        ]
    )

    assert stats["longest_loss_streak"] == 3
    assert stats["current_win_streak"] == 0
    assert stats["current_loss_streak"] == 3
