def is_palindrome(phrase):
    
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

    

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    phrase = "".join(phrase.split()).lower()
    if phrase == phrase[::-1]:
        return True
    return False


print(is_palindrome('tacocat'))
 
print(is_palindrome('Noon'))
print(is_palindrome('noon'))
 

print(is_palindrome('robert'))
print(is_palindrome('taco cat'))
 