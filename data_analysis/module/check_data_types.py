def type_check(expected_types):
    def decorator(func):
        def wrapper(*args):
            for arg, expected in zip(args[1:], expected_types):
                if not isinstance(arg, expected):
                    raise TypeError(f"Expected {expected} but got {type(arg)}")
            return func(*args)
        return wrapper
    return decorator
