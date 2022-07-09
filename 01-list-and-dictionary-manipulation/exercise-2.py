value = None # Just to avoid undefined value errors

my_dict = {
    'id': 292, 
    'name': 'Ralf', 
    'age': 33, 
    49: 'Wibble'
}

# 1. Write an expression to fetch the value 'Ralf' from my_dict
#    value = my_dict[SOMETHING-GOES-HERE]

assert value == 'Ralf'

# 2. Write an expression to fetch the value 33 from my_dict
#    value = my_dict[SOMETHING-GOES-HERE]

assert value == 33

# 3. Write an expression to fetch the value 'Wibble' from my_dict
#    value = my_dict[SOMETHING-GOES-HERE]

assert value == 'Wibble'

# 4. Now change the above three exercises to use the dict.get() 
#    method to fetch their values
#
#    Hint: see https://devdocs.io/python/library/stdtypes#dict.get

# 5. What happens if we try to fetch the value for a key that 
#    doesn't exist...
#
#    a) Using dict[key] syntax?       - e.g. my_dict['banana']
#    b) Using the dict.get() method?  - e.g. my_dict.get('banana')
#
#    (If you don't know, try it out)

# 6. Write a statement to add a new entry to my_dict, so that the 
#    following assertions are satisfied

#    a) A string...

assert my_dict['favourite_colour'] == 'Blue'

#    b) An int...

assert my_dict['step_count'] == 8185

#    c) A list...

assert my_dict['books'] == ['Ulysses', 'War and Peace', 'Lord of the Rings']

#    Do you now understand that you can store any data type as a
#    value in a dictionary? :)
