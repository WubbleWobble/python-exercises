"""Exercise 2"""

from typing import Dict

def products_summary() -> Dict:
    """
    Fetches product data from the database and turns it into
    the format our application needs for the products_summary
    screen
    """

    # 1. Use the "get_product_data" from db.py to fetch the data from the database
    # 2. Transform the data into the format below so that our application can use it

    return {
        'Beans': {
            'weight': 320,
            'stock_count': 850,
        },
        'Soup': {
            'weight': 340,
            'stock_count': 1120,
        },
        'Bagels': {
            'weight': 200,
            'stock_count': 120,
        },
        'Biscuits': {
            'weight': 350,
            'stock_count': 230,
        },
    }