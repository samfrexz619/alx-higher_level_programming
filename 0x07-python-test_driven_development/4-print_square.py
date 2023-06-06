#!/usr/bin/python3
'''function that prints square with char #

'''



def print_square(size):
    '''function that prints square with char #

    Args:
        size: size of the square printed

    Returns:
        nth

    Raises:
        TypeError: if size isnt an int
        ValueError: if size < 0

    '''


    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for idx in range(size):
        print('#' * size)
