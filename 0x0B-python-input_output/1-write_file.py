#!/usr/bin/python3
'''module that writes to a txt file'''


def write_file(filename="", text=""):
    '''func that rets char count

    Args:
        filename: filename
        text: text to write

    Raises:
        Exception: when file can be opened

    '''

    count_char = 0

    with open(filename, mode='w', encoding='utf-8') as f:
        count_char = f.write(text)

    return count_char
