import itertools
print("Input the number(n):")
n = int(input())
result = sum(
    (0 <= n - (i + j + k) <= 9)
    for i, j, k in itertools.product(range(10), range(10), range(10))
)
print("Number of combinations:", result)
