#!/usr/bin/python3
import random
number = random.randint(-10, 10)
for i in number:
    if i>0:
        print(f"{i:d}: is positive")
    elif i==0:
        print(f"{i:d}: is zero")
    else:
        print(f"{i:d}: is negative")
