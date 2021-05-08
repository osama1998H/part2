
s1, s2, d = map(int, input(
    "Input Two Adjoined Sides And The Diagonal Of A Parallelogram:").split())

if (s1 ** 2) + (s2 ** 2) == (d ** 2):
    print("Parallelogram Is Rectangle")
elif s1 == s2:
    print("Parallelogram Is Rhombus")
