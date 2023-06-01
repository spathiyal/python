def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    word = []
    for letter in phrase:
        
            if letter.isupper() and letter.lower()== to_swap.lower():  
                word.append(letter.lower())
            elif letter.islower() and letter.lower()== to_swap.lower():
                 word.append(letter.upper())
            else:
                 word.append(letter)
    return (''.join(word))
print(flip_case('Aaaahhh', 'A'))
print(flip_case('Aaaahhh', 'h'))
print(flip_case('Aaaahhh', 'a'))