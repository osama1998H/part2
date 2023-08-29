def odd_check(number: int) -> bool:
    """[summary]

    Args:
        number (int): [positive number]

    Returns:
        bool: [Return True If The Number Is Odd And False If The Number Is Even]
    """
    return number % 2 != 0


x = [1, 3, 8, 6, 7, 4, 9, 10, 14]
y = sorted(x)

# ? [1, 3, 4, 6, 7, 8, 9, 10]


def calc_median(y: list) -> int:
    """[summary]

    Args:
        y ([list]): [Data Array For Calculate Median]

    Returns:
        int: [Return Int > Median]
    """
    if odd_check(len(y)):
        n = (len(y)-1)/2
        m = y[int(n)]
    else:
        n = len(y) // 2
        m = (y[n-1] + y[n]) / 2
    print(f"median of {y} is: {m}")
    return m


calc_median(y)
