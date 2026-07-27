"""
Tests for the HAPT Market Scanner.
"""

from app.scanner.market_scanner import MarketScanner


def test_new_scanner_is_empty():
    scanner = MarketScanner()

    assert scanner.symbols == []


def test_load_symbols():
    scanner = MarketScanner()

    symbols = ["MES", "MNQ", "SPY"]

    scanner.load_symbols(symbols)

    assert scanner.symbols == symbols


def test_load_empty_symbols():
    scanner = MarketScanner()

    scanner.load_symbols([])

    assert scanner.symbols == []


def test_validate_supported_symbols():
    scanner = MarketScanner()

    scanner.load_symbols(["MES", "MNQ", "GC"])

    valid = scanner.validate_symbols()

    assert valid == ["MES", "MNQ", "GC"]


def test_validate_mixed_symbols():
    scanner = MarketScanner()

    scanner.load_symbols([
        "MES",
        "XYZ",
        "MNQ",
        "ABC",
        "GC",
    ])

    valid = scanner.validate_symbols()

    assert valid == [
        "MES",
        "MNQ",
        "GC",
    ]


def test_validate_all_invalid():
    scanner = MarketScanner()

    scanner.load_symbols([
        "AAA",
        "BBB",
        "CCC",
    ])

    assert scanner.validate_symbols() == []


def test_get_valid_instruments():
    scanner = MarketScanner()

    scanner.load_symbols([
        "MES",
        "MNQ",
    ])

    instruments = scanner.get_valid_instruments()

    assert len(instruments) == 2

    assert instruments[0]["name"] == "Micro E-mini S&P 500"
    assert instruments[0]["exchange"] == "CME"

    assert instruments[1]["name"] == "Micro E-mini Nasdaq-100"
    assert instruments[1]["exchange"] == "CME"


def test_get_valid_instruments_ignores_invalid():
    scanner = MarketScanner()

    scanner.load_symbols([
        "MES",
        "ABC",
        "MNQ",
    ])

    instruments = scanner.get_valid_instruments()

    assert len(instruments) == 2


def test_scan_empty_list(capsys):
    scanner = MarketScanner()

    scanner.scan()

    captured = capsys.readouterr()

    assert "Starting market scan..." in captured.out
    assert "Market scan complete." in captured.out


def test_scan_single_symbol(capsys):
    scanner = MarketScanner()

    scanner.load_symbols(["MES"])

    scanner.scan()

    captured = capsys.readouterr()

    assert "Scanning MES..." in captured.out


def test_scan_multiple_symbols(capsys):
    scanner = MarketScanner()

    scanner.load_symbols([
        "MES",
        "MNQ",
        "GC",
    ])

    scanner.scan()

    captured = capsys.readouterr()

    assert "Scanning MES..." in captured.out
    assert "Scanning MNQ..." in captured.out
    assert "Scanning GC..." in captured.out