#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    sliced_list = my_list[:x]

    for idx in sliced_list:
        try:
            print(f'{idx:d}', end='')
        except TypeError:
            pass
        except ValueError:
            pass
        else:
            count += 1

    print()
    return (count)
