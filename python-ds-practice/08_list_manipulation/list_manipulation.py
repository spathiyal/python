def list_manipulation(lst, command, location, value=None):
    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'remove', 'end')
        3

        >>> list_manipulation(lst, 'remove', 'beginning')
        1

        >>> lst
        [2]

    add: add item at beginning/end, and return list

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'add', 'beginning', 20)
        [20, 1, 2, 3]

        >>> list_manipulation(lst, 'add', 'end', 30)
        [20, 1, 2, 3, 30]

        >>> lst
        [20, 1, 2, 3, 30]

    Invalid commands or locations should return None:

        >>> list_manipulation(lst, 'foo', 'end') is None
        True

        >>> list_manipulation(lst, 'add', 'dunno') is None
        True
    """
    val = []
    if(command == 'add' and location == 'beginning'):
         print('1', command,location,value)
         val = lst.insert(0, value)
         print ("val",lst)
    elif (command == 'add' and location == 'end'):
        print('2', command,location,value)
        val = lst.append(value)
    elif (command == 'remove' and location == 'beginning'):
        print('3', command,location)
        val =  lst.pop(0)
    elif(command == 'remove' and location == 'end'):
        print('4', command,location)
        val =lst.pop(lst.length-1)
    
    else:
        val = None
    return val

lst = [1, 2, 3]
# print(list_manipulation(lst, 'add', 'dunno') )
# print(list_manipulation(lst, 'foo', 'end'))
print(list_manipulation(lst, 'add', 'end', 30))
print(list_manipulation(lst, 'add', 'beginning', 20))
 
