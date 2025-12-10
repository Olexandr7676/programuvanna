from functools import wraps
from inspect import signature

def check_types(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        sig = signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()

        for name, value in bound_args.arguments.items():
            if name in func.__annotations__:
                expected_type = func.__annotations__[name]
                if not isinstance(value, expected_type):
                    raise TypeError(
                        f"Argument '{name}' must be {expected_type}, got {type(value)} instead."
                    )
        return func(*args, **kwargs)
    return wrapper
