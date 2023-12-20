#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    res = None
    try:
        res = fct(*args)
    except Exception as er:
        sys.stderr.write("Exception: {}\n".format(er))
        return None
    finally:
        return res
