#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        new_tup = (length, None)
    else:
        new_tup = (length, sentence[0])
    return (new_tup)
