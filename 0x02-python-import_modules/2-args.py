#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv
    count = len(argv) - 1

    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
        print("1: {}".format(argv[count]))
    else:
        print("{} arguments:".format(count))
        for x in range(count):
            print("{}: {}".format(x + 1, argv[x + 1]))
