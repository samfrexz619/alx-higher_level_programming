#!/usr/bin/python3
def uppercase(str):
    for idx in range(len(str)):
        if ord(str[idx]) >= 97 and ord(str[idx]) <= 122:
            n = 32
        else:
            n = 0

        print('{:c}'.format(ord(str[idx]) - n), end='')
    print()
