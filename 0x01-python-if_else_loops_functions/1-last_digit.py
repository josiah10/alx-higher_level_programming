#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = int(repr(number)[-1])
if number >= 0:
    last = number % 10
else:
    last = number % -10
    if last > 5:
        print(f"Last digit of {number:d} is {last:d} and is greater than 5")
    elif last != 0 and last < 6:
        print(f"Last digit of {number:d} is {last:d} and is less "
              "than 6 and not 0")
    else:
        print(f"Last digit of {number:d} is {last:d} and is 0")
