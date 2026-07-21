"""
HAPT Logger
-----------
Configures the application's logging system.
"""

import logging


def setup_logger():
    """Configure and return the HAPT logger."""

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    logger = logging.getLogger("HAPT")
    logger.info("HAPT is ready. Awaiting commands...")

    return logger