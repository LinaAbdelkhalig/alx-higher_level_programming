#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = set()
    for i in my_list:
        unique.add(i)

    sum = 0
    for x in unique:
        sum += x

    return sum
