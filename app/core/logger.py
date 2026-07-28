"""
HAPT Logger
-----------
Configures the application's logging system.
"""

import logging


def setup_logger() -> logging.Logger:
    """Configure and return the HAPT application logger."""

    logger = logging.getLogger("HAPT")

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler()

    handler.setFormatter(
        logging.Formatter(
            fmt="%(asctime)s | %(levelname)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
    )

    logger.addHandler(handler)
    logger.propagate = False

    logger.info("HAPT is ready. Awaiting commands...")

    return logger