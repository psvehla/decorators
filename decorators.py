"""My decorators."""


def do_twice(func):
    """Do twice."""
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice
