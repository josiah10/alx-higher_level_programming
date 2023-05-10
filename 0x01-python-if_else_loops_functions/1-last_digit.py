mport random
number = random.randint(-10000, 10000)
last = abs(number) % 10
if number < 0:
    last = -digit
    print("Last digit of {} is {} and is ".format(number, digit), end="")
    if last > 5:
        print("greater than 5")
    elif last == 0:
        print("0")
    else:
        print("less than 6 and not 0")
