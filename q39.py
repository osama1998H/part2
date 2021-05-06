x1, y1, x2, y2, x3, y3 = map(float, input(
    "enter x1 y1 x2 y2 x3 y3 values: ").split())
print(x1, y1, x2, y2, x3, y3)

a = (x1*(y2-y3) - y1*(x2 - x3) + (x2*y3) - (x3*y2))
b = (x1**2 + y1**2) * (y3-y2) + (x2**2 + y2**2)* (y1 - y3)+ (x3**2 + y3**2)* (y2 - y1)
c = (x1**2 + y1**2) * (x2-x3) + (x2**2 + y2**2)* (x3 - x1)+ (x3**2 + y3**2)* (x1 - x2)
d = (x1**2 + y1**2) * (x3*y2 - x2 *y3) + (x2**2 + y2**2) * (x1*y3 - x3 *y1) + (x3**2 + y3**2) * (x2*y1 - x1 *y3)
x = -(b/ (2*a))
y = -(c/(2*a))
from math import sqrt

r = sqrt(((b**2) + (c**2) - (4*a*d))/ 4*(a**2))

print(f"radios: {sqrt(r)}")
print(f"x, y: {x}, {y}")
# print(f"radios: ")
# print(f"radios: ")
