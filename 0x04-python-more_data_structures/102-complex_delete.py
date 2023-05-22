#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_k = list(a_dictionary.keys())

    for vd in list_k:
        if value == a_dictionary.get(vd):
            del a_dictionary[vd]

    return (a_dictionary)
