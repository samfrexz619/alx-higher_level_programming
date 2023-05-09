#!/usr/bin/python3
def remove_char_at(str, n):
    t = ''
    for idx in range(len(str)):
        if idx != n:
            t = t + str[idx]

    return (t)
