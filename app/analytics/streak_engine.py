"""
HAPT Winning & Losing Streak Engine
-----------------------------------

Calculates winning and losing streaks
from completed trade results.
"""


class StreakEngine:
    """Calculates trading streak statistics."""

    @staticmethod
    def calculate(
        trade_results: list[float],
    ) -> dict:
        """
        Calculate streak statistics.

        Parameters
        ----------
        trade_results : list[float]
            Positive = win
            Negative = loss
            Zero = break-even (resets streak)

        Returns
        -------
        dict
        """

        longest_win = 0
        longest_loss = 0

        current_win = 0
        current_loss = 0

        for result in trade_results:

            if result > 0:

                current_win += 1
                current_loss = 0

            elif result < 0:

                current_loss += 1
                current_win = 0

            else:

                current_win = 0
                current_loss = 0

            longest_win = max(
                longest_win,
                current_win,
            )

            longest_loss = max(
                longest_loss,
                current_loss,
            )

        return {
            "longest_win_streak": longest_win,
            "longest_loss_streak": longest_loss,
            "current_win_streak": current_win,
            "current_loss_streak": current_loss,
        }
