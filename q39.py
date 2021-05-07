from math import sqrt
import numpy as np
x1, y1, x2, y2, x3, y3 = map(float, input(
    "enter x1 y1 x2 y2 x3 y3 values: ").split())
print(x1, y1, x2, y2, x3, y3)

a = np.array([[x1, x2, x3], [y1, y2, y3], [1, 1, 1]])

b = -np.array([
    [x1**2 + y1**2, x2**2 + y2**2, x3**2 + y3**2],
    [y1, y2, y3],
    [1, 1, 1]
])
c = np.array([
    [x1**2 + y1**2, x2**2 + y2**2, x3**2 + y3**2],
    [x1, x2, x3],
    [1, 1, 1]
])
d = -np.array([
    [x1**2 + y1**2, x2**2 + y2**2, x3**2 + y3**2],
    [x1, x2, x3],
    [y1, y2, y3]
])


a = np.linalg.det(a)
b = np.linalg.det(b)
c = np.linalg.det(c)
d = np.linalg.det(d)

x = round(-(b/(2*a)), 3)
y = round(-(c/(2*a)), 3)

a_s = a**2
b_s = b**2
c_s = c**2



r = sqrt(((b_s + c_s / 4 * a_s) - d / a))


print(x, y, sqrt(r))
