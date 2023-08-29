import time

def my_fuc(n):
    return [i**0.5 for i in range(int(n))]


start = time.time()
my_fuc(400000)
my_fuc(400000)
my_fuc(400000)
my_fuc(400000)
my_fuc(400000)
end = time.time()
print(f"time: {round(end-start, 4)}")