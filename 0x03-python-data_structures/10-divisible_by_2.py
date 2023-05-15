#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if_divisible = []

    for idx in range(len(my_list)):
        if my_list[idx] % 2 == 0:
            if_divisible.append(True)
        else:
            if_divisible.append(False)
    
    return (if_divisible)
