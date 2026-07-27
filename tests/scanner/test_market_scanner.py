"""
Tests for the HAPT Market Scanner.
"""

from app.scanner.market_scanner import MarketScanner


def test_new_scanner_is_empty():
    """A new scanner should contain no symbols."""

    scanner = MarketScanner()

    assert scanner.symbols == []


def test_load_symbols():
    """Symbols should be loaded into the scanner."""

    scanner = MarketScanner()

    symbols = [
        "MES",
        "MNQ",
        "SPY",
    ]

    scanner.load_symbols(symbols)

    assert scanner.symbols == symbols


def test_load_empty_symbols():
    """Loading an empty list should work."""

    scanner = MarketScanner()

    scanner.load_symbols([])

    assert scanner.symbols == []


def test_scan_empty_list(capsys):
    """Scanner should handle an empty symbol list."""

    scanner = MarketScanner()

    scanner.scan()

    captured = capsys.readouterr()

    assert "Starting market scan..." in captured.out
    assert "Market scan complete." in captured.out


def test_scan_single_symbol(capsys):
    """Scanner should print one symbol."""

    scanner = MarketScanner()

    scanner.load_symbols(["MES"])

    scanner.scan()

    captured = capsys.readouterr()

    assert "Scanning MES..." in captured.out


def test_scan_multiple_symbols(capsys):
    """Scanner should print every loaded symbol."""

    scanner = MarketScanner()

    symbols = [
        "MES",
        "MNQ",
        "SPY",
    ]

    scanner.load_symbols(symbols)

    scanner.scan()

    captured = capsys.readouterr()

    for symbol in symbols:
        assert f"Scanning {symbol}..." in captured.out