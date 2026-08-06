"""
Tests for the HAPT Correlation Analysis Engine.
"""

from app.portfolio.correlation_analysis import (
    CorrelationAnalysisEngine,
    CorrelationPair,
)


def make_pairs():
    return [
        CorrelationPair("EMA", "VWAP", 0.85),
        CorrelationPair("EMA", "ORB", 0.40),
        CorrelationPair("VWAP", "ORB", -0.25),
    ]


def test_matrix_generation():
    matrix = CorrelationAnalysisEngine.matrix(
        make_pairs()
    )

    assert matrix["EMA"]["EMA"] == 1.0
    assert matrix["VWAP"]["VWAP"] == 1.0
    assert matrix["ORB"]["ORB"] == 1.0

    assert matrix["EMA"]["VWAP"] == 0.85
    assert matrix["VWAP"]["EMA"] == 0.85


def test_lookup_forward():
    value = CorrelationAnalysisEngine.lookup(
        make_pairs(),
        "EMA",
        "VWAP",
    )

    assert value == 0.85


def test_lookup_reverse():
    value = CorrelationAnalysisEngine.lookup(
        make_pairs(),
        "VWAP",
        "EMA",
    )

    assert value == 0.85


def test_lookup_missing():
    value = CorrelationAnalysisEngine.lookup(
        make_pairs(),
        "EMA",
        "Unknown",
    )

    assert value is None


def test_highly_correlated():
    results = (
        CorrelationAnalysisEngine.highly_correlated(
            make_pairs()
        )
    )

    assert len(results) == 1
    assert results[0].strategy_a == "EMA"
    assert results[0].strategy_b == "VWAP"


def test_empty_pairs():
    matrix = CorrelationAnalysisEngine.matrix([])

    assert matrix == {}

    results = (
        CorrelationAnalysisEngine.highly_correlated([])
    )

    assert results == []
