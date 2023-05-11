#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    print('{2} + {1} = {0}'.format(add(a, b), b, a))
    print('{} - {} = {}'.format(a, b, sub(a, b)))
    print('{} * {} = {}'.format(a, b, mul(a, b)))
    print('{} / {} = {}'.format(a, b, div(a, b)))
