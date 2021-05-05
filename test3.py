import time

def my_fuc(n):
    data = []
    for i in range(int(n)):
        data.append(i**0.5)
    return data


start = time.time()
my_fuc(400000)
my_fuc(400000)
my_fuc(400000)
my_fuc(400000)
my_fuc(400000)
end = time.time()
print(f"time: {round(end-start, 4)}")