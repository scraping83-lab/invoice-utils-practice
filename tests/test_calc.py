from invoice_utils import format_currency, subtotal, tax, total


def test_subtotal_single_line():
    assert subtotal([(2, 19.99)]) == 39.98


def test_subtotal_multiple_lines():
    assert subtotal([(1, 10.00), (3, 2.50)]) == 17.50


def test_subtotal_empty():
    assert subtotal([]) == 0


def test_tax_default_rate():
    assert tax(100.00) == 8.75


def test_tax_custom_rate():
    assert tax(100.00, rate=0.10) == 10.00


def test_total_includes_tax():
    assert total([(1, 100.00)]) == 108.75


def test_format_currency():
    assert format_currency(1234.5) == "$1,234.50"


def test_format_currency_zero():
    assert format_currency(0) == "$0.00"
