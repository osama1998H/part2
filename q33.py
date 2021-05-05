def sum_two_digits(x: int, y: int) -> int:
    """[summary]

    Args:
        x (int): [First Number]
        y (int): [Seconed Number]

    Returns:
        int: [Return The Numbers Of Digits Of The Sum Value]
    """
    result = x + y
    return(len(str(result)))


print(f"The Sun Digits Of A And B: {sum_two_digits(4, 3)}")
