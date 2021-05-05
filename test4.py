import time
from numba import njit


def my_fuc(n):
    data = []
    for i in range(int(n)):
        data.append(i**0.5)
    return data


start = time.time()
njit(my_fuc(400000), my_fuc(50000), my_fuc(50000), my_fuc(50000), my_fuc(50000))
end = time.time()
print(f"time: {round(end-start, 4)}")
