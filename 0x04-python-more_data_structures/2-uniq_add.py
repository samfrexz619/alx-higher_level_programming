#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = set(my_list)
    sum = 0

    for idx in new_list:
        sum += idx
    return (sum)
