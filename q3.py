x = [1, -6, 4, 2, -1, 2, 0, -2, 0]

for i in range(len(x)):
    if i == len(x)-2:
        break
    if (x[i] + x[i+1] + x[i+2]) == 0:
        print([x[i], x[i+1], x[i+2]])
