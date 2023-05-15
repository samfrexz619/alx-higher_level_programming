#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)

    if length == 0:
        return (None)

    max_list = my_list[0]

    for idx in range(1, length):
        if my_list[idx] > max_list:
            max_list = my_list[idx]

    return (max_list)
