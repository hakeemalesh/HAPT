"""
HAPT Trading Rules
------------------

This module contains the global trading rules used
throughout the HAPT Trading System.

Every engine should import its thresholds from here
instead of hard-coding numbers.

This gives HAPT one single source of truth.
"""


class TradingRules:
    """Global HAPT trading rules."""

    # ----------------------------------
    # EMA Trend
    # ----------------------------------

    EMA_ALIGNMENT_SCORE = 20

    # ----------------------------------
    # RSI
    # ----------------------------------

    RSI_BULLISH = 60
    RSI_BEARISH = 40
    RSI_SCORE = 15

    # ----------------------------------
    # MACD
    # ----------------------------------

    MACD_SCORE = 15

    # ----------------------------------
    # VWAP
    # ----------------------------------

    VWAP_SCORE = 20

    # ----------------------------------
    # Relative Volume
    # ----------------------------------

    RELATIVE_VOLUME_HIGH = 1.20
    RELATIVE_VOLUME_SCORE = 15

    # ----------------------------------
    # ATR Volatility
    # ----------------------------------

    # ATR quality scores
    ATR_GOOD_SCORE = 10
    ATR_FAIR_SCORE = 5
    ATR_POOR_SCORE = 0

    # ATR quality thresholds
    # These are relative values and may be
    # adjusted later for different markets.
    ATR_FAIR_THRESHOLD = 0.50
    ATR_GOOD_THRESHOLD = 1.00
    # ----------------------------------
    # Session
    # ----------------------------------

    SESSION_MAX_SCORE = 15

    # ----------------------------------
    # Grades
    # ----------------------------------

    GRADE_A_PLUS = 95
    GRADE_A = 90
    GRADE_B = 80
    GRADE_C = 70

    # ----------------------------------
    # Maximum Score
    # ----------------------------------

    MAX_SCORE = 100