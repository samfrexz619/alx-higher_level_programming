#!/usr/bin/python3
'''module to create pascal triangle'''


def pascal_triangle(n):
    '''function taht creates pascal triangle

    Arg:
        n: int
    '''
    res = []
    c = []

    if n <= 0:
        return res
    for idx in range(n):
        if idx == 0:
            c.append(1)
            res.append(c)
        elif idx == 1:
            c = c + [1]
            res.append(c)
        else:
            w = []
            w.append(c[0])
            for i in range(len(c) - 1):
                tot = 0
                tot = c[i] + c[i + 1]
                w.append(tot)
            w.append(c[-1])
            c = w
            res.append(c)
    return res
