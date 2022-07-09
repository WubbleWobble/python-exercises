value = None # Just to avoid undefined value errors

couriers = [
    {'id': 151, 'name': 'Rar'},
    {'id': 213, 'name': 'Daisy'},
    {'id': 232, 'name': 'Mason'},
    {'id': 304, 'name': 'Bob'},
]

# 1. Write a statement to fetch a value from the list above
#    such that the following assertion is satisfied:

assert value == {'id': 232, 'name': 'Mason'}

# 2. Write a statement to fetch a value from the list above
#    such that the following assertion is satisfied:

assert value == 'Bob'

# 3. Write a statement to CHANGE the list above so that the
#    following assertion is satisfied:

assert couriers[2]['name'] == 'Wobble'

# 4. Write a statement to CHANGE the list above so that the
#    following assertion is satisfied:

assert couriers[0]['id'] == '22'

# 5. Write a statement to ADD a new entry to the list above
#    so that the following assertions are satisfied:

#    N.B. It's intended that your one statement which adds
#         a new entry will satisfy all three of these assertions

#    Hint: What type of data structure is "couriers"?
assert len(couriers) == 5
assert couriers[4]['name'] == 'Rar'
assert couriers[4]['id'] == 123
