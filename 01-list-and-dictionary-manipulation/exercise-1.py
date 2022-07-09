value = None # Just to avoid undefined value errors

my_list = [
    'apple',
    'banana',
    'pear',
    'orange'
]

# 1. Write an expression to fetch the value 'apple' from my_list
#    value = my_list[SOMETHING-GOES-HERE]

assert value == 'apple'

# 2. Write an expression to fetch the value 'orange' from my_list
#    value = my_list[SOMETHING-GOES-HERE]

assert value == 'orange'

# 3. Write an expression to modify the list above so that the
#    following assertion is satisfied:

assert my_list[2] == 'pineapple'

# 4. Write an expression to add an entry to the list above so
#    that the following assertion is satisfied:

assert my_list[4] == 'melon'