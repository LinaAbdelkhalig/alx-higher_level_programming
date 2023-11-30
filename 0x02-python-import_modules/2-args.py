#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argnum = len(sys.argv[1:])
    if argnum == 1:
        print(f"{argnum} argument:".format(sys.argv[1:]))
        print(f"1: {sys.argv[1]}".format(sys.argv[1]))
    elif argnum == 0:
        print(f"{argnum} arguments.".format(argnum))
    else:
        print(f"{argnum} arguments:".format(argnum))
        for i in range(len(sys.argv[1:])):
            print(f"{i + 1}: {sys.argv[i + 1]}".format(i + 1, sys.argv[i + 1]))
