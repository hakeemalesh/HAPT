"""
HAPT Volume Analysis
--------------------

Provides volume-related calculations.
"""


class Volume:
    """Performs volume analysis."""

    @staticmethod
    def average(volumes):
        """
        Calculate average volume.
        """

        if not volumes:
            return None

        return round(sum(volumes) / len(volumes), 2)

    @staticmethod
    def relative(current_volume, volumes):
        """
        Calculate Relative Volume (RVOL).

        Returns
        -------
        float | None
        """

        average_volume = Volume.average(volumes)

        if average_volume in (None, 0):
            return None

        return round(
            current_volume / average_volume,
            2
        )

    @staticmethod
    def is_high_volume(current_volume, volumes, threshold=1.5):
        """
        Return True if current volume is above
        the specified RVOL threshold.
        """

        rvol = Volume.relative(
            current_volume,
            volumes
        )

        if rvol is None:
            return False

        return rvol >= threshold