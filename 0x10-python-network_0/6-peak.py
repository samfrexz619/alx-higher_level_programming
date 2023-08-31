#!/usr/bin/python3
'''Finds the peak'''


def find_peak(list_of_integers):
    if list_of_integers == []:
        return None

    lnt = len(list_of_integers)
    mid = int(lnt / 2)
    ls = list_of_integers

    if mid - 1 < 0 and mid + 1 >= lnt:
        return ls[mid]
    elif mid - 1 < 0:
        return ls[mid] if ls[mid] > ls[mid + 1] else ls[mid + 1]
    elif mid + 1 >= lnt:
        return ls[mid] if ls[mid] > ls[mid - 1] else ls[mid - 1]

    if ls[mid - 1] < ls[mid] > ls[mid + 1]:
        return ls[mid]

    if ls[mid + 1] > ls[mid - 1]:
        return find_peak(ls[mid:])
    return find_peak(ls[:mid])
