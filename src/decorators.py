"""My decorators."""
import functools
import time


def do_twice(func):
    """Do twice."""
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice


def timer(func):
    """Print the run time of the decorated function."""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()  # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()    # 2
        run_time = end_time - start_time  # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer


def decorator(func):
    """Boilerplate for a decorator."""
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do somehting before
        value = func(*args, **kwargs)
        # Do somehting before
        return value
    return wrapper_decorator
