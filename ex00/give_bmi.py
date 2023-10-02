def give_bmi(
        height: list[int or float],
        weight: list[int or float]
) -> list[int or float]:
    """
    Takes in a list of height and a list of weight, and return
    the BMI value.

    Parameters:
    param1 (height: list[int or float]): List of height.
    param2 (weight: list[int or float]): List of weight.

    Returns:
    list[int or float]: A list of either int of float as BMI value.
    """
    assert len(height) == len(weight), "invalid heght and weight length"
    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            raise AssertionError("arguments must be type int or float")
    return [w / (h ** 2) for h, w in zip(height, weight)]


def apply_limit(bmi: list[int or float], limit: int) -> list[bool]:
    '''
    Takes in a list of BMI value and a limit, and return a list
    of booleans on whether the BMI value exceeded the limit.

    Parameters:
    param1 (bmi: list[int or float]): List of BMI value.
    param2 (limit: int): Limit value.

    Returns:
    list[bool]: A boolean on whether the input BMI value exceeded
    limit.
    '''
    return [b > limit for b in bmi]
