#!/usr/bin/python3
if name __ = __main
    import sys

    n = len(sys.argv)
    length = (len(sys.argv) - 1)
    if length == 0:
        print(f"{length} arguments.")
    elif length == 1:
        print(f"{length} arguments:")
        for i in range(1, n):
            print(f"{i:d}: {sys.argv[i]}")

    else:
        print(f"{length} arguments:")
        for i in range(1, n):
            print(f"{i:d}: {sys.argv[i]}")

