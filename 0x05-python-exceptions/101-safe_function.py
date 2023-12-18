#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return (fct(*args))
    except Exception as er:
        print("Exception:", er, file=sys.stderr)
        return None
