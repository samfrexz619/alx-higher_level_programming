#!/usr/bin/python3
def no_c(my_string):
    new_str = ''
    for idx in my_string:
        if idx == 'c' or idx == 'C':
            idx = ''
        new_str += idx
    return (new_str)
