#!/usr/bin/python3
for alph in reversed(range(97, 123)):
    print(f'{alph if (alph % 2 == 0) else (alph - 32):c}', end='')
