#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(f"{} is positive",.format(number))
elif number == 0:
    print(f"{} is zero",.format(number))
elif number < 0:
    print(f"{} is negative",.format(number))
