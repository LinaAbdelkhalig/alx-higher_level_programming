#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argsum = 0
    for i in range(len(sys.argv[1:])):
        argsum += int(sys.argv[i + 1])
    print(f"{argsum}".format(argsum))
