#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dkeys = list()
    for key in a_dictionary.keys():
        dkeys.append(key)
    dkeys.sort()
    for key in dkeys:
        print("{}: {}".format(key, a_dictionary[key]))
