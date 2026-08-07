"""
HAPT Main Entry Point
---------------------

Starts the Hybrid AI Trading Platform.
"""

from app.core.banner import show_banner
from app.core.hapt_engine import HAPTEngine
from app.core.logger import setup_logger
from app.core.startup import run_startup_checks


def main():
    """
    Start the HAPT application.
    """

    logger = setup_logger()

    show_banner()

    run_startup_checks()

    logger.info(
        "Launching HAPT Engine."
    )

    engine = HAPTEngine()

    engine.run()

    logger.info(
        "HAPT finished successfully."
    )


if __name__ == "__main__":
    main()