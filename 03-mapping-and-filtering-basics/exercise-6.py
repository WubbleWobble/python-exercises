from typing import Dict, List, Union

products = [
    {
        'id': 35,
        'name': 'Banana',
        'price': 0.25,
    },
    {
        'id': 75,
        'name': 'Cabbage',
        'price': 0.45,
    },
    {
        'id': 101,
        'name': 'Carrot',
        'price': 0.15,
    },
]

def find_product_by_id(product_id: int, products: List) -> Union[Dict, None]:
    # Write code here so that when given a list of products and a
    # product_id, this function returns:
    # 
    # a) the matching product's dictionary, if a product with the 
    #    given id exists
    #
    # b) "None" if no product with that id exists
    pass

cabbage = find_product_by_id(75, products)
assert cabbage['name'] == 'Cabbage'

silly = find_product_by_id(10101, products)
assert silly is None