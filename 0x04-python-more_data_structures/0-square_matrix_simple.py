#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_mat = list(matrix)

    for idx in range(len(matrix)):
        new_mat[idx] = list(map(lambda n: n**2, matrix[idx]))
    return (new_mat)
