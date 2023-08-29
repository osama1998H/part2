while True:
    n = int(input("enter the number (0 exit): "))
    if n == 0:
        break
    a = [int(input("enter the seq ns: ")) for _ in range(n)]
    count = sum(a)
    print(count)
