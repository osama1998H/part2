

number_string = input("Enter Your Phone Number: ")


def check_miss_numbers(number_string: str) -> list:
    """[summary]

    Args:
        number_string (str): [Phone Number For Cheack]

    Returns:
        list: [The Mising Numbers In Phone Numbers]
    """
    miss_numbers = []
    orginals_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    numbers = [int(i) for i in number_string]
    for check in orginals_numbers:
        if check in numbers:
            pass
        else:
            miss_numbers.append(check)
    return miss_numbers


def main():
    print(check_miss_numbers(number_string))


if __name__ == "__main__":
    main()
