"""My decorators."""
import functools
import time
from flask import redirect, url_for, request
from flask_login import current_user


PLUGINS = dict()


def do_twice(func):
    """Do twice."""
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice


def repeat(num_times):
    """Repeat the function the specified number of times."""
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    return decorator_repeat


def repeat2(_func=None, *, num_times=2):
    """Repeat the function the specified or default number of times."""
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat

    if _func is None:
        return decorator_repeat
    else:
        return decorator_repeat(_func)


def repeat3(_func=None, *, num_times=2):
    """Repeat the function the specified or default number of times."""
    if _func is None:
        return functools.partial(repeat3, num_times=num_times)

    @functools.wraps(_func)
    def wrapper_repeat(*args, **kwargs):
        for _ in range(num_times):
            value = _func(*args, **kwargs)
        return value
    return wrapper_repeat


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


def debug(func):
    """Print the function signature and return value."""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")
        return value
    return wrapper_debug


def slow_down(func):
    """Sleep 1s before calling the function."""
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        value = func(*args, **kwargs)
        return value
    return wrapper_slow_down


def count_calls(func):
    """Count the number of calls to this decorator. A stateful decorator."""
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
        return func(*args, **kwargs)
    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls


def login_required(func):
    """Ensure user is logged in before proceeding."""
    @functools.wraps(func)
    def wrapper_login_required(*args, **kwargs):
        if not current_user.is_authenticated:
            return redirect(url_for("login", next=request.url))
        return func(*args, **kwargs)
    return wrapper_login_required


def decorator(func):
    """Boilerplate for a decorator."""
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do somehting before
        value = func(*args, **kwargs)
        # Do somehting after
        return value
    return wrapper_decorator


def register(func):
    """Register a function as a plugin."""
    PLUGINS[func.__name__] = func
    return func
