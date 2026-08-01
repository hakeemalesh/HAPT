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

    VWAP_GOOD_SCORE = 10
    VWAP_POOR_SCORE = 0

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
    ATR_FAIR_THRESHOLD = 0.50
    ATR_GOOD_THRESHOLD = 1.00

    # ----------------------------------
    # Market Structure
    # ----------------------------------

    MARKET_STRUCTURE_GOOD_SCORE = 5
    MARKET_STRUCTURE_POOR_SCORE = 0

    # ----------------------------------
    # Session
    # ----------------------------------

    SESSION_MAX_SCORE = 15

    # ----------------------------------
    # Grades
    # ----------------------------------

    # Calibrated after Strategy Engine v1
    # to reflect realistic high-quality
    # futures trading opportunities.

    GRADE_A_PLUS = 90
    GRADE_A = 80
    GRADE_B = 65
    GRADE_C = 50

    # ----------------------------------
    # Maximum Score
    # ----------------------------------

    MAX_SCORE = 100