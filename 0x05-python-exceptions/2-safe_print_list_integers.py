#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0

    for idx in my_list[:x]:
        try:
            print(f'{idx:d}', end='')
        except TypeError:
            pass
        except ValueError:
            continue
        else:
            count += 1

    print()
    return (count)
