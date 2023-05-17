#!/usr/bin/python3
def number_keys(a_dictionary):
    n = 0
    new_keys = list(a_dictionary.keys())

    for idx in new_keys:
        n += 1

    return (n)
