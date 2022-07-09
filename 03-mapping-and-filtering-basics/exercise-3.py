from typing import List


def shouts(things: List) -> List:
    # Write code here so that the assertion below is satisfied
    
    # Hint: See https://devdocs.io/python~3.10/library/stdtypes#str.upper
    pass

input = ['apple', 'banana', 'cabbage']
actual = shouts(input)

assert actual == ['APPLE', 'BANANA', 'CABBAGE']
