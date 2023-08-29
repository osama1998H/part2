
def gen_strobogrammatic(n):
    """
    :type n: int
    :rtype: List[str]
    """
    return helper(n, n)


def xdata(a, v):
    if a > v:
        return a
    xdata(a + 1, v - 1)
    


def helper(n, length):
    if n == 0:
        return [""]
    if n == 1:
        return ["1", "0", "8"]
    middles = helper(n-2, length)
    result = []
    for middle in middles:
        if n != length:
            result.append(f"0{middle}0")
        result.extend((f"8{middle}8", f"1{middle}1", f"9{middle}6", f"6{middle}9"))
    return result


# print("n = 2: \n", gen_strobogrammatic(2))
# print("n = 3: \n", gen_strobogrammatic(3))
# print("n = 110: \n", gen_strobogrammatic(4))

print(xdata(15, 20))
