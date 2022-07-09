from typing import List

def bigger_than_five(numbers: List) -> List:
    # Write code here so that the assertion below is satisfied

    # Hint: Same as before, except that something we'll add things
    #       to the new list, and sometimes we won't
    pass

input = [2, 6, 4, 12, 15]
actual = bigger_than_five(input)

assert actual == [6, 12, 15]
