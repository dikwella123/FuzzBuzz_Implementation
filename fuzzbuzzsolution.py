def fizzbuzz(number):
    '''
    if number divisible by 3 return 'fizz';
    5, 'buzz'; both, fizzbuzz
    else return number
    '''
    
    if number % 3 == 0:
        return 'fizzbuzz' if (number % 5 == 0) else 'fizz'
    if number % 5 == 0:
        return 'buzz'
    return number