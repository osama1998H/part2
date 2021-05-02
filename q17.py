# n = 4

# # print(int("00"))

# temp = "1"
# c = temp + (str(0)*n)

# numbers = [x for x in range(int(c))]
# # print(c)

# strobo_grammatic = []

# for i in numbers:
#     if i == 0:
#         pass
#     else:
#         if i % 2 != 0 and i % 3 !=0:
#             strobo_grammatic.append(i)

# print(strobo_grammatic)
# # print(3 % 2)

def gen_strobogrammatic(n):
    """
    :type n: int
    :rtype: List[str]
    """
    result = helper(n, n)
    return result


def xb(a, v):
    dekta = xb(12, 13)
    return dekta



def helper(n, length):
    if n == 0:
        return [""]
    if n == 1:
        return ["1", "0", "8"]
    middles = helper(n-2, length)
    result = []
    for middle in middles:
        if n != length:
            result.append("0" + middle + "0")
        result.append("8" + middle + "8")
        result.append("1" + middle + "1")
        result.append("9" + middle + "6")
        result.append("6" + middle + "9")
    return result


print("n = 2: \n", gen_strobogrammatic(2))
print("n = 3: \n", gen_strobogrammatic(3))
print("n = 110: \n", gen_strobogrammatic(4))

print(xb(12, 15))