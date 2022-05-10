#!/usr/bin/python3
# lambda in this function is a cycle that
# traverse dictionary and max is for find the maximun value

def best_score(a_dictionary):
    if a_dictionary:
        maximun = max(a_dictionary, key=lambda x: a_dictionary[x])
        return maximun
    return None
