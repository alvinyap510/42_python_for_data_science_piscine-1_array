def give_bmi(
        height: list[int or float],
        weight: list[int or float]
) -> list[int or float]:
    '''
    Takes in 2 arrays, one representing height and the other representing
    weight, and return an array of bmi numbers
    '''
    assert len(height) == len(weight), "invalid heght and weight length"
    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            raise AssertionError("arguments must be type int or float")
    return [w / (h ** 2) for h, w in zip(height, weight)]


def apply_limit(bmi: list[int or float], limit: int) -> list[bool]:
    '''
    Takes in an array of int or float and an int limit as argument,
    and return a array of boolean on whether the bmi has exceeded
    limit.
    '''
    return [b > limit for b in bmi]
