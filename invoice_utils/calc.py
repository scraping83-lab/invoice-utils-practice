"""Core invoice calculations: subtotal, tax, total, and currency formatting."""

TAX_RATE = 0.0875


def subtotal(lines):
    """Return the subtotal for a list of (quantity, unit_price) line items."""
    return round(sum(quantity * unit_price for quantity, unit_price in lines), 2)


def tax(amount, rate=TAX_RATE):
    """Return the tax on an amount at the given rate."""
    return round(amount * rate, 2)


def total(lines, rate=TAX_RATE):
    """Return the invoice total: subtotal plus tax."""
    return round(subtotal(lines) + tax(subtotal(lines), rate), 2)


def format_currency(amount):
    """Format an amount as a USD currency string."""
    return f"${amount:,.2f}"
