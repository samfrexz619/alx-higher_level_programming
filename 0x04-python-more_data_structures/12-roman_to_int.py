#!/usr/bin/python3
def subtract(num):
    sub = 0
    max_ls = max(num)

    for idx in num:
        if max_ls > idx:
            sub += idx

    return (max_ls - sub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return (0)

    rom_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    new_keys = list(rom_num.keys())

    num = 0
    l_rom = 0
    ls_num = [0]

    for c in roman_string:
        for k_num in new_keys:
            if k_num == c:
                if rom_num.get(c) <= l_rom:
                    num += subtract(ls_num)
                    ls_num = [rom_num.get(c)]
                else:
                    ls_num.append(rom_num.get(c))
                l_rom = rom_num.get(c)

    num += subtract(ls_num)

    return (num)
