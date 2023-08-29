def getzeros(n):
    x = list(range(n))

    count = 1

    for n in x:
        count *= (n+1)
    result = str(count)
    if result[-1] == "0":
        if result[-2] == "0":
            print(2)
        else:
            print(1)
    # print(x, len(x), count, result.count("0"))


getzeros(5)
getzeros(12)
getzeros(100)
