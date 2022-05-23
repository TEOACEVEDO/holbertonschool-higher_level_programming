#!/usr/bin/python3
def raise_exception():
    a = 7
    if not type(a) is str:
        raise TypeError()
