#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv) - 1
    print("{} argument{}{}"
            .format(length, "" if length == 1 else "s", "." if length == 0 else ":"))
    i = 1
    while i <= length:
        print("{}: {}".format(i, sys.argv[i]))
        i += 1
