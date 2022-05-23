#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    f, count = 0, 0
    while f < x:
        try:
            print("{:d}".format(my_list[f]), end="")
            count += 1
        except(TypeError, ValueError):
            pass
        finally:
            f += 1
    print()
    return count
