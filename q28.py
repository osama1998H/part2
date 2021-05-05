series = [(i+5.3)/2 for i in range(1, 16)]


def Series_info(series: list) -> dict:
    """[summary]

    Args:
        series (list): [Array Of Series]

    Attribute:
        third_term (flout): \n
        third_last_term (flout): \n
        sum_of_the_series (flout): \n


    Returns:
        dict: [Series Information]
    """
    third_term = series[2]
    third_last_term = series[-3]
    sum_of_the_series = 0
    for i in series:
        sum_of_the_series += i
    info = {
        "Third Term": third_term,
        "Third Last Term": third_last_term,
        "Sum Of The Series": sum_of_the_series,
        "Series": series
    }
    return info


info = Series_info(series)

for key in info:
    print(f"{key}:-> ({info[key]})")
