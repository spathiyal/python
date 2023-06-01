"""Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """

def last_element(lst):
     if len(lst) == 0:
          return None
     return lst[len(lst)-1]



print(last_element([1, 2, 5,9]))
print(last_element([]))