#!/usr/bin/python3
'''
    algo that solves the N-queen puzzle

'''


def is_safe(pos_queen, nqueen):
    ''' method to det if the queen can or cant kill each other

        Args:
            pos_queen: arr that has the queens position
            nqueen: queen num

        Returns:
            True: if queens cant kill each other
            False: if some of the queens can kill

        '''

        for idx in range(nqueen):

            if pos_queen[idx] == pos_queen[nqueen]:
                return False

            if abs(pos_queen[idx] - pos_queen[nqueen]) == abs(idx - nqueen):
                return False

        return True

def print_res(pos_queen, nqueen):
    '''method to print list with the queen's positions

    Args:
        pos_queen: arr that has the queens position
        nqueen: queen num


    '''

    res = []

    for idx in range(nqueen):
        res.append([idx, pos_queen[idx]])

    print(res)


def 
