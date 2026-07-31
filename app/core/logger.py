"""
HAPT Logger
-----------

Configures the application's logging system.
"""

import logging


def setup_logger() -> logging.Logger:
    """
    Configure and return the HAPT application logger.
    """

    logger = logging.getLogger("HAPT")

    #
    # Prevent duplicate handlers
    #
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler()

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    handler.setFormatter(formatter)

    logger.addHandler(handler)

    #
    # Prevent messages propagating to the root logger
    #
    logger.propagate = False

    logger.info(
        "HAPT logging initialized successfully."
    )

    return logger