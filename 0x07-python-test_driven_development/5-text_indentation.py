#!/usr/bin/python3
def text_indentation(text):
    if not type(text) is (str):
        raise TypeError("text must be a string")

    for i in text:
        if i in ['.', '?', ':']:
            print(i, end='')
            print()
            print()
        else:
            print(i, end='')
