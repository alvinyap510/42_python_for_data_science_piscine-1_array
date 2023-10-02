def give_bmi(height: list[int or float], weight: list[int or float]) -> list[int or float]:
    if len(height) != len(weight):
        raise AssertionError("the arguments are bad")
    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            raise AssertionError("the arguments are bad")
    return [w / (h ** 2) for h, w in zip(height, weight)]


def apply_limit(bmi: list[int or float], limit: int) -> list[bool]:
    return [b > limit for b in bmi]
