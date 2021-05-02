

def sqrt(a):
    return a**(1/2)


def pherhaghors(a, b):
    c = sqrt((a**2) + (b**2))
    return round(c, 3)


print(pherhaghors(4.2, 3.12))
