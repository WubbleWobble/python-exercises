"""Exercise 1"""

from typing import Dict

def cash_vs_card() -> Dict:
    """
    Fetches cash_vs_card data from the database and turns it into
    the format that our application needs
    """

    # 1. Use the "get_cash_vs_card_data" from db.py to fetch the data from the database
    # 2. Transform the data into the format below so that our application can use it

    return {
        'CASH': 436,
        'CARD': 229,
    }