#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    uniq = set(my_list)
    for i in uniq:
        sum += i
    return sum
