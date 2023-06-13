#!/usr/bin/python3
'''module that contains a function to read from file'''


def read_file(filename=""):
    '''function that reads from file

    Arg:
        filename: file to be read

    Raises:
        Exception: when the file can be opened

    '''

    with open(filename, encoding='utf-8') as f_to_read:
        print(f_to_read.read(), end='')
