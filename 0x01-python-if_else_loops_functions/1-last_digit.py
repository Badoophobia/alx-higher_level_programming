#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    value = number % 10
elif number < 0:
    temp = -number
    value = -(temp % 10)
elif number == 0:
    value = 0
var = "Last digit of"
while True:
    if value > 5:
        print(f"Last digit of {number:d} is {value:d} and is greater than 5")
    elif value == 0:
        print(f"Last digit of {number:d} is {value:d} and is 0")
    elif value < 6 and not 0:
        print(f"{var} {number:d} is {value:d} and is less than 6 and not 0")
    break
