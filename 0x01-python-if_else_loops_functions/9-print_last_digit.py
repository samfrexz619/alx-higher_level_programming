#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        last_dig = number % 10
    else:
        last_dig = number % -10
        last_dig *= -1

    print(f'{last_dig:d}', end='')
    return (last_dig)
