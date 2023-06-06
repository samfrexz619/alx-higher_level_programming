#!/usr/bin/python3
'''function that prints two new line after '.?:' char

'''



def text_indentation(text):
    '''function that prints 2 new lines after '.?:'

    Args:
        text: input str

    Returns:
        nth

    Raises:
        TypeError: if text isnt a str

    '''


    if type(text) is not str:
        raise TypeError('text must be a string')

    c = text[:]

    for i in '.?:':
        l_text = c.split(i)
        c = ''
        for ix in l_text:
            ix = ix.strip(' ')
            c = ix + i if c is '' else c + '\n\n' + ix + i

    print(c[:-3], end='')
