"""
HAPT Volume Tests
-----------------

Unit tests for Volume calculations.
"""

import unittest

from indicators.volume import Volume


class TestVolume(unittest.TestCase):
    """Tests for Volume."""

    def test_average_empty(self):
        """Average volume of an empty list."""

        self.assertIsNone(
            Volume.average([])
        )

    def test_average(self):
        """Average volume calculation."""

        volumes = [100, 200, 300]

        self.assertEqual(
            Volume.average(volumes),
            200.0
        )

    def test_relative_volume(self):
        """Relative volume calculation."""

        volumes = [100, 200, 300]

        self.assertEqual(
            Volume.relative(
                300,
                volumes
            ),
            1.5
        )

    def test_high_volume_true(self):
        """Detect high volume."""

        volumes = [100, 200, 300]

        self.assertTrue(
            Volume.is_high_volume(
                300,
                volumes
            )
        )

    def test_high_volume_false(self):
        """Detect normal volume."""

        volumes = [100, 200, 300]

        self.assertFalse(
            Volume.is_high_volume(
                200,
                volumes
            )
        )


if __name__ == "__main__":
    unittest.main()