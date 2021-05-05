

def progression_type(data: list) -> tuple:
    """[summary]

    Args:
        data (list): [Array Of Data Or Progression]

    Returns:
        tuple: [Progression Type]
    """
    data = sorted(data)
    for n in range(len(data)):
        if data[n] - data[n+1] == data[n+1] - data[n + 2]:
            d = data[n] - data[n+1]
            data.append(data[-1] + abs(d))
            return "AP", data
        elif data[n + 1] / data[n] == data[n + 2] / data[n + 1]:
            d = data[n + 1] / data[n]
            data.append(data[-1] * int(abs(d)))
            return "GP", data
        else:
            return "The Data Not In Any Progression Pattren"


data = [2, 4, 8, 16, 32]

data2 = [i*3 for i in range(10)]

print(progression_type(data))
print(progression_type(data2))
print(type(progression_type(data)))
