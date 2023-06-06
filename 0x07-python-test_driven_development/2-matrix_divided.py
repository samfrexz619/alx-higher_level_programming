#!/usr/bin/python3
'''
    function that divides the num of matrix

'''


def matrix_divided(matrix, div):
    '''function that divided int/float num of a matrix

    Args:
        matrix: lists of int/float
        div: num that divided the matrix

    Returns:
        A new matrix

    Raises:
        TypeError: if the elem of the matrix isn't a list
                   if the elem of the list isnt int/float
                   if the list of the matrix doesnt arent of the same size
                   if div isnt an int/float num

        ZeroDivisionError: if div is zero

    '''


    if not type(div) in (int, float):
        raise TypeError('div must be a num')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    mssg = 'matrix must be a matrix (list of lists) of integers/floats'

    if not matrix or not isinstance(matrix, list):
        raise TypeError(mssg)

    e_len = 0
    mssg = 'Each row of the matrix must have the same size'

    for ele in matrix:
        if not ele or not isinstance(ele, list):
            raise TypeError(mssg)

        if e_len != 0 and len(ele) != e_len:
            raise TypeError(mssg)

        for i in ele:
            if not type(i) in (int, float):
                raise TypeError(mssg)

        e_len = len(ele)

    v = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (v)
