#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for idx in range(len(matrix)):
        for idx1 in range(len(matrix[idx])):
            if idx1 != 0:
                print(' ', end='')
            print('{:d}'.format(matrix[idx][idx1]), end='')
        print()
