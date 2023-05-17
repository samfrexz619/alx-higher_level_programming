#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ordered_list = list(a_dictionary.keys())
    ordered_list.sort()
    for idx in ordered_list:
        print("{}: {}".format(idx, a_dictionary.get(idx)))
