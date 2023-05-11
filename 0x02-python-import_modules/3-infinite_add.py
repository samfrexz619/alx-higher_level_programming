#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    num = len(sys.argv)
    res = 0

    if num >= 1:
        for idx in range(1, num):
            res += int(sys.argv[idx])

    print(f'{res:d}')
