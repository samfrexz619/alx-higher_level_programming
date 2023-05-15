#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    length_a = len(tuple_a)
    length_b = len(tuple_b)

    if length_a == 0:
        a = 0
        b = 0
    elif length_a == 1:
        a = tuple_a[0]
        b = 0
    else:
        a = tuple_a[0]
        b = tuple_a[1]

    if length_b == 0:
        c = 0
        d = 0
    elif length_b == 1:
        c = tuple_b[0]
        d = 0
    else:
        c = tuple_b[0]
        d = tuple_b[1]

    total = (a + c, b + d)
    return (total)
