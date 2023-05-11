#!/usr/bin/python3
if __name__ == '__main__':
    from add_0 import add
    a = 1
    b = 2
    print('{1} + {0} = {2}'.format(b, a, add(a, b)))
