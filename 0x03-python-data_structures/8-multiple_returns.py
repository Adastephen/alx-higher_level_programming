#!/usr/bin/python3
def multiple_returns(sentence):
    new_tuple = 0
    new_tuple += len(sentence)
    sec_tuple = sentence[0]
    if new_tuple == 0:
        sec_tuple = None
        return (sec_tuple)
    else:
        return (new_tuple, sec_tuple)
