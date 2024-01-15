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
    def decorator_repeat2(func):
        @functools.wraps(func)
        def wrapper_repeat2(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat2

    if _func is None:
        return decorator_repeat2
    else:
        return decorator_repeat2(_func)


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


def slow_down2(_func=None, *, rate=1):
    """Sleep the desired number of seconds before calling the function."""
    def decorator_slow_down2(func):
        @functools.wraps(func)
        def wrapper_slow_down2(*args, **kwargs):
            time.sleep(rate)
            return func(*args, **kwargs)
        return wrapper_slow_down2

    if _func is None:
        return decorator_slow_down2
    else:
        return decorator_slow_down2(_func)


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


def singleton(cls):
    """Make a class a Singleton."""
    @functools.wraps(cls)
    def wrapper_singleton(*args, **kwargs):
        if not wrapper_singleton.instance:
            wrapper_singleton.instance = cls(*args, **kwargs)
        return wrapper_singleton.instance
    wrapper_singleton.instance = None
    return wrapper_singleton


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


class Counter:
    """A counter decorator class."""

    def __init__(self, start=0):
        self.count = start

    def __call__(self):
        """Increment count and report count. Callable for decorator to work."""
        self.count += 1
        print(f"Current count is {self.count}")


class CountCalls:
    """A decorator class that counts calls to a function."""

    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        """
        Increment call count and report call count and function name.

        Callable for decorator to work.
        """
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)
