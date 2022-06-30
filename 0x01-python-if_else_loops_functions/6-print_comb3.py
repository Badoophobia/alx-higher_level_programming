#!/usr/bin/python3
for i in range(0, 9):
    for j in range(1, 10):
        if i == 0 and j <= 0:
            continue
        elif i == 1 and j <= 1:
            continue
        elif i == 2 and j <= 2:
            continue
        elif i == 3 and j <= 3:
            continue
        elif i == 4 and j <= 4:
            continue
        elif i == 5 and j <= 5:
            continue
        elif i == 6 and j <= 6:
            continue
        elif i == 7 and j <= 7:
            continue
        elif i == 8 and j <= 8:
            continue
        elif i <= 7 and j <= 9:
            print("{}{},".format(i, j), end=" ")
        else:
            print("{}{}".format(i, j))
