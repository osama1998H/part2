while True:
    n = int(input("enter the number (0 exit): "))
    if n == 0:
        break
    a = []
    for i in range(n):
        a.append(int(input("enter the seq ns: ")))
    count = 0
    for i in a:
        count += i 
    print(count)
