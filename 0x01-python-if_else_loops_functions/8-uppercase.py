#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) in range(65, 81):
            continue
        elif ord(i) not in range(65, 91):
            if ord(i) in range(97, 123):
                char = ord(i) - 32
            else:
                char = ord(i)
            print("{}".format(chr(char)), end="")
    print("\n", end="")
