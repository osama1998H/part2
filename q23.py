
from cyberbrain import trace


# @trace
# def sum_count(n):
#     counter = 0
#     for i in range(n+1):
#         counter += i

#     return counter


# # print(sum_count(10))
# @trace
# def subtract_numbers(n):
#     m = n - sum_count(n)
#     if m < 0:
#         return m
#     else:
#         subtract_numbers(m)


# # print(subtract_numbers(-2))

# for i in range(2, 10):
#     print(subtract_numbers(i))


def repeat_times(n):
    s = 0
    n_str = str(n)
    while (n > 0):
        n -= sum([int(i) for i in list(n_str)])
        n_str = list(str(n))
        s += 1
    return s


print(repeat_times(9))
print(repeat_times(21))
