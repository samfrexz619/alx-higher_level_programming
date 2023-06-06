#!/usr/bin/python3
'''
    algo that solves the N-queen puzzle

'''


def safe(pos_queen, nqueen):
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


def back_track(pos_queen, nqueen):
    '''function to exec the backtracking algo

    Args:
        pos_queen: arr that has the queens pos
        mqueen: queen num

    '''

    if nqueen is len(pos_queen):
        print_res(pos_queen, nqueen)
        return

    pos_queen[nqueen] = -1

    while((pos_queen[nqueen] < len(pos_queen) - 1)):

        pos_queen[nqueen] += 1

        if safe(pos_queen, nqueen) is True:

            if nqueen is not len(pos_queen):
                back_track(pos_queen, nqueen + 1)


def solve_queen(size):
    '''function to invoke the backtracking algo

    Arg:
        size: chessboard size

    '''

    pos_queen = [-1 for idx in range(size)]

    back_track(pos_queen, 0)


if __name__ == '__main__':

    import sys

    if len(sys.argv) == 1 or len(sys.argv) > 2:
        print('Usage: nqueens N')
        sys.exit(1)

    try:
        size = int(sys.argv[1])
    except:
        print('N must be a number')
        sys.exit(1)

    if size < 4:
        print('N must be at least 4')
        sys.exit(1)

    solve_queen(size)
