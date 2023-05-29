#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0

    for idx in range(x):
        try:
            print(f'{my_list[idx]:d}', end='')
        except TypeError:
            pass
        except ValueError:
            pass
        else:
            count += 1

    print()
    return (count)
