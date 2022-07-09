value = None # Just to avoid undefined value errors

huge = {
    'things': [
        'Cake',
        'Doughnut',
        'Jelly',
    ],
    'orders': [
        {
            'id': 12, 
            'customer_id': 234, 
            'products': [
                {'name': 'Ball', 'quantity': 3},
                {'name': 'Kite', 'quantity': 34}
            ]
        },
        {
            'id': 2, 
            'customer_id': 43, 
            'products': [
                {'name': 'Monitor', 'quantity': 1},
                {'name': 'Mouse', 'quantity': 7},
                {'name': 'YubiKey', 'quantity': 4}
            ]
        }
    ],
}

# 1. Write a statement to fetch a value from the dict above
#    such that the following assertions are satisfied:

#    a) 
assert value == 'Jelly'

#    b) 
assert value == 43

#    c) 
assert value == {'name': 'Kite', 'quantity': 34}

#    d)
assert value == 'Ball'

#    e)
assert value == 4