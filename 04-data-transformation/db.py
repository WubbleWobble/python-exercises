"""Mock database routines"""

from typing import Tuple

def get_cash_vs_card_data() -> Tuple:
    """Fetches cash_vs_card data from the database"""
    return (
        (436, 'CASH'),
        (229, 'CARD'),
    )

def get_product_data() -> Tuple:
    """Fetches product data from the database"""
    return (
        # (id, name, weight, manufacturer, stock_count)
        (1, 'Beans', 320, 'Hubels', 850),
        (12, 'Soup', 340, 'Heinz', 1120),
        (42, 'Bagels', 200, 'Warburton', 120),
        (75, 'Biscuits', 350, 'WobbleTech', 230),
    )
