#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    sliced_list = my_list[:x]
    count = 0

    for idx in sliced_list:
        try:
            print('{}'.format(idx), end='')
        except Exception:
            break
        else:
            count += 1

    print()
    return (count)
