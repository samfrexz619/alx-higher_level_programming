#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = list(my_list)
    length = len(new_list) - 1

    if idx < 0:
        return (my_list)
    elif idx > length:
        return (my_list)
    else:
        new_list[idx] = element
    return (new_list)
