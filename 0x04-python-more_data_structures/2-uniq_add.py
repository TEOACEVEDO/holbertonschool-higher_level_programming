#!/usr/bin/python3
def uniq_add(my_list=[]):
    # The set() function creates a set object.
    # The items in a set list are unordered, so
    # it will appear in random order. but when
    # used on an existing list it deletes the duplicates
    list = set(my_list)
    sum = 0
    for i in list:
        sum += i
    return sum
