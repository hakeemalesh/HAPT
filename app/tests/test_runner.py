"""
HAPT Test Runner
----------------

Runs all HAPT unit tests.
"""

import unittest


def run():
    """
    Discover and execute all tests.
    """

    loader = unittest.TestLoader()

    suite = loader.discover(
        start_dir="tests",
        pattern="test_*.py"
    )

    runner = unittest.TextTestRunner(
        verbosity=2
    )

    return runner.run(suite)


if __name__ == "__main__":
    run()