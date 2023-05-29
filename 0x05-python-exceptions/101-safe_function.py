#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        res = fct(*args)
    except Exception as idx:
        sys.stderr.write("Exception: {}\n".format(idx))
        res = None

    return (res)
