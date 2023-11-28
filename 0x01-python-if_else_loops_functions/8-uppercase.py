#!/usr/bin/python3
def uppercase(str):
    str_cp = ""
    for c in str:
        if ord(c) in range(97, 123):
            c = chr(ord(c) - 32)
            str_cp += c
        else:
            str_cp += c
    print(f"{str_cp}".format(str_cp))
