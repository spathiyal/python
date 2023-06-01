def partition(lst, fn):
    """Partition lst by predicate.
     
     - lst: list of items
     - fn: function that returns True or False
     
     Returns new list: [a, b], where `a` are items that passed fn test,
     and `b` are items that failed fn test.

        >>> def is_even(num):
        ...     return num % 2 == 0
        
        >>> def is_string(el):
        ...     return isinstance(el, str)
        
        >>> partition([1, 2, 3, 4], is_even)
        [[2, 4], [1, 3]]
        
        >>> partition(["hi", None, 6, "bye"], is_string)
        [['hi', 'bye'], [None, 6]]
    """

    l1 = []
    l2 = []
    finalLst = []
    for x in lst:
        if fn == is_even:
            if is_even(x):
               l1.append(x)

            else:
               l2.append(x)
        else:
            if is_string(x):
               l1.append(x)
            else:
               l2.append(x)
    finalLst.append(l1)   
    finalLst.append(l2)
    return   finalLst
def is_even(num):
        return num % 2 == 0
        
def is_string(el):
        return isinstance(el, str)

print(partition([1, 2, 3, 4], is_even))
print(partition(["hi", None, 6, "bye"], is_string))