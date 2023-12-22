"""Some code that demonstrates how decorators work in Python."""
import math
import random
from datetime import datetime
from src.decorators import do_twice, timer, debug, slow_down, register, PLUGINS


def my_decorator(func):
    """Add some output before and after the function."""
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


def not_during_the_night(func):
    """Stay quiet at night."""
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass  # Hush, the neighbours are asleep.
    return wrapper


def say_whee():
    """Say 'Whee!'."""
    print("Whee!")


@my_decorator
def say_whee_with_pie():
    """Say 'Whee!' with pie (syntactic sugar)."""
    print("Whee!")


@do_twice
def say_whee_twice():
    """Say 'Whee!' twice."""
    print("Whee!")


@do_twice
def greet(name):
    """Say hello in a personalised way."""
    print(f"Hello, {name}.")


@do_twice
def return_greeting(name):
    """Return a personalised greeting message."""
    print("Creating greeting")
    return f"Hi {name}."


@timer
def waste_some_time(num_times):
    """Kill some time."""
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])


@debug
def make_greeting(name, age=None):
    """Make a greeting based on name and maybe age."""
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you are growing up!"


# Apply a decorator to a standard library function.
math.factorial = debug(math.factorial)


def approximate_e(terms=18):
    """Approximate e."""
    return sum(1 / math.factorial(n) for n in range(terms))


@slow_down
def countdown(from_number):
    """Countdown from the given number."""
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)


@register
def say_hello(name):
    """Say hello."""
    return f"Hello {name}."


@register
def be_awesome(name):
    """Declare our awesomeness."""
    return f"Yo {name}, together we are awesome!"


def randomly_greet(name):
    """Greet in an unpredictable way."""
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f"Using {greeter!r}")
    return greeter_func(name)


say_whee = my_decorator(say_whee)
say_whee = not_during_the_night(say_whee)
