from typing import List

def say_hello(names: List) -> List:
    # Write code here so that the assertion below is satisfied
    
    # Hint: See https://realpython.com/python-f-strings/#f-strings-a-new-and-improved-way-to-format-strings-in-python
    pass

input = ['Wibble', 'Wobble', 'Banana']
actual = say_hello(input)

assert actual == ['Hello Wibble', 'Hello Wobble', 'Hello Banana']
