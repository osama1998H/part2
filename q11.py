def sum_array(*args: list, target: int):
    """[summary]

    Args:
        *args (list): [List Or Lists Contain The Numbers For Count It With Target]
        target (int): [The Number You Wana To Compaite It With Results]

    Returns:
        If Equls Lists And Target\n
        e.x\n
        x = [10, 11, 12, 13, 14, 15]\n
        y = [10, 11, 12, 13, 14, 15]\n
        z = [10, 11, 12, 13, 14, 15]\n
        target = 225

        If Not Equls Return Messges
    """
    count = 0
    results = []
    for list in args:
        for item in list:
            count += item
        results.append(count)
        count = 0

    result_sum = sum(results)
    if result_sum == target:
        for res in args:
            print(res)
        print(f"target = {target}")
    else:
        print("The Arrays And Target Not Equles")


x = list(range(10, 16))
y = list(range(10, 16))
z = list(range(10, 16))

sum_array(x, y, z, target=(75 * 3))
