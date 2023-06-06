#!/usr/bin/python3
'''function that prints a message
'''


def say_my_name(first_name, last_name=""):
    '''function that prints '<first name> <last name>'

    Args:
        first_name: first name
        last_name: last name

    Returns:
        nth

    Raises:
        TypeError: if first name or last name isnt a str

    '''


    if type(first_name) is not str:
        raise TypeError('first_name must be a string')

    if type(last_name) is not str:
        raise TypeError('last_name must be a string')

    print(f'My name is {first_name},{last_name}')
