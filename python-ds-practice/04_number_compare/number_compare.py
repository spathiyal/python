def number_compare(a, b):

    if a> b:
       msg = 'First is greater'
    elif a<b:
        msg = 'Second is greater'
    else:
        msg = 'Numbers are equal'
    return msg
    """Report on whether a>b, b>a, or b==a
    
        >>> number_compare(1, 1)
        'Numbers are equal'
        
        >>> number_compare(-1, 1)
        'Second is greater'
        
        >>> number_compare(1, -2)
        'First is greater'
    """

print(number_compare(1, 1))
print(number_compare(1, 5))
print(number_compare(6, 1))