#!/usr/bin/python3
# list(map()) could be useful to fill a list also
# creates a new list and applies the function to each element
def multiply_list_map(my_list=[], number=0):
    return list(map(lambda x: x * number, my_list))
