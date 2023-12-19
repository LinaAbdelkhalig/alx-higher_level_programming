#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        for u in range(x):
            print(my_list[u], end="")
            i += 1
        print("")
    except IndexError:
        print("")
    return i
