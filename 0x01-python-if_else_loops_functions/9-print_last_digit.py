#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        tmp = -number
        value = tmp % 10
        print(value, end="")
        return value
    else:
        value = number % 10
        print(value, end="")
        return value
