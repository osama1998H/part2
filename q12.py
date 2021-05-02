import numpy as np
from itertools import product

c = (1, 2, 3)


x = list(product("abcdf", "abcdf", "abcdf"))

for i in x:
    print(i)

print(len(x))
