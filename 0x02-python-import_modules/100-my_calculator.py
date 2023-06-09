#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    num = len(sys.argv) - 1
    if num != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)

    opt = sys.argv[2]
    if opt != '+' and opt != '-' and opt != '*' and opt != '/':
        print('Unknown operator. Available operators: +, -, * and /')
        sys.exit(1)

    from calculator_1 import add, sub, mul, div
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if opt == '+':
        print(f'{a} + {b} = {add(a, b)}')
    elif opt == '-':
        print(f'{a} - {b} = {sub(a, b)}')
    elif opt == '*':
        print(f'{a} * {b} = {mul(a, b)}')
    else:
        print(f'{a} / {b} = {div(a, b)}')
