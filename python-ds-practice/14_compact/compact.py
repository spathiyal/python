def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    validType =[int,str]
    return [x for x  in lst if type(x) in validType and x!= 0]
   


print(compact([0, 1, 2, '', [], False, (), None, 'All done']))
 