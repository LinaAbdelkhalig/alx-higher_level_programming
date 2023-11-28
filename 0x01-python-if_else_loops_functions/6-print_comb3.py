#!/usr/bin/python3
for i in range(9):
    for j in range(10):
        if i != j and j > i:
            if i == 8 and j == 9:
                print(f"{i}{j}".format(i, j))
            else:
                print(f"{i}{j}, ".format(i, j), end="")
