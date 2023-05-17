#!/usr/bin/python3
def search_replace(my_list, search, replace):
    curr_list = list(map(lambda n: replace if n == search else n, my_list))
    return (curr_list)
