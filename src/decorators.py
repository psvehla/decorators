"""My decorators."""
import functools


def do_twice(func):
    """Do twice."""
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice


def decorator(func):
    """Boilerplate for a decorator."""
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do somehting before
        value = func(*args, **kwargs)
        # Do somehting before
        return value
    return wrapper_decorator
