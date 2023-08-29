x, y = 99, 120


def common_advisor(x: int, y: int) -> int:
    """[summary]

    Args:
        x (int): [First Value]
        y (int): [Second Value]

    Returns:
        int: [Common Advisor]
    """
    x_factor = []
    y_factor = []

    x_factor = {i for i in range(1, x+1) if x % i == 0}
    y_factor = {i for i in range(1, y+1) if y % i == 0}

    difference_y = y_factor.difference(x_factor)
    difference_x = x_factor.difference(y_factor)
    union = y_factor.union(x_factor)
    result = union - difference_x - difference_y
    return max(result)


print(common_advisor(x, y))
