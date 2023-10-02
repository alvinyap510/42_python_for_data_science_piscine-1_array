import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    '''
    Takes in a list and return a truncated list.

    Parameters:
    param1 (family: list): A list that will be truncated.
    param2 (start: int): Starting index.
    param3 (end: int): Ending index.
    
    Returns:
    list: The list that has been truncated.
    '''
    assert isinstance(family, list), "first param must be a list is"
    for f in family:
        dimension = len(family[0])
        assert isinstance(f, list), "non-list child detected"
        assert len(f) == dimension, "all childs must have same dimension"
    print(f"My shape is : {np.array(family).shape}")
    new_family = family[start:end]
    print(f"My new shape is : ({np.array(new_family).shape})")
    return new_family
