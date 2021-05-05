
from math import sqrt


def triangle_type(a, b, c):
    if sqrt(c**2) == sqrt(a**2 + b**2):
        print("Yes")
    elif sqrt(b**2) == sqrt(a**2 + c**2):
        print("Yes")
    elif sqrt(a**2) == sqrt(c**2 + b**2):
        print("Yes")
    else:
        print("No")


triangle_type(4, 5, 3)
