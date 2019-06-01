def assert_number(arg):
    if not isinstance(arg, (int, float)):
        raise TypeError(f"Expected number, got {type(arg)}")
