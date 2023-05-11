#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    num = len(sys.argv) - 1

    if num == 0:
        print(f'{num} arguments.')
    elif num == 1:
        print(f'{num} argument:')
    else:
        print(f'{num} arguments:')

    if num >= 1:
        for idx in range(0, num):
            print(f'{idx + 1}: {sys.argv[idx + 1]}')
