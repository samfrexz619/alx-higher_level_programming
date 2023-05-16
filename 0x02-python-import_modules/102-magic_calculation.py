#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub

    if a < b:
        t = add(a, b)
        for idx in range(4, 6):
            t = add(t, idx)
        return (t)
    else:
        return (sub(a, b))
