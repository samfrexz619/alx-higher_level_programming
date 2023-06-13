#!/usr/bin/python3
'''module that writes to a txt file'''


def write_file(filename="", text=""):
    '''func that rets char count

    Args:
        filename: file
        text: text

    '''

    count_char = 0

    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(text)

    with open(filename, mode='r', encoding='utf-8') as file_r:
        word_l = file_r.read()

        for i in word_l.split():
            count_char += len(i)

    return count_char
