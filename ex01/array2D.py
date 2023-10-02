def slice_me(family: list, start: int, end: int) -> list:
    assert isinstance(family, list), "arguments are bad"
    for f in family:
        child_length = len(family[0])
        assert isinstance(f, list), "arguments are bad"
        assert len(f) == child_length, "arguments are bad"
    print(f"My shape is : ({len(family)}, {child_length})")
    new_family = family[start:end]
    print(f"My new shape is : ({len(new_family)}, {child_length})")
    return new_family
