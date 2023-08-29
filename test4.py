import time
from numba import njit


def my_fuc(n):
    return [i**0.5 for i in range(int(n))]


start = time.time()
njit(my_fuc(400000), my_fuc(50000), my_fuc(50000), my_fuc(50000), my_fuc(50000))
end = time.time()
print(f"time: {round(end-start, 4)}")
