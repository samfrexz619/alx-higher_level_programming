#!/usr/bin/python3
'''
    this module is a function that adds two integer
'''


def add_integer(a, b=98):
    '''function that adds two int

    Args:
        a: first num
        b: second num

    Returns:
        the sum of two numbers

    Raises:
        TypeError: if a or b are not int and/or float num

    '''


    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError('a must be an integer')
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')
    a = int(a)
    b = int(b)
    return (a + b)
