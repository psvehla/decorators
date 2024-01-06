"""Some code that demonstrates how decorators work in Python."""
import math
import random
from datetime import datetime
from flask import Flask
from dataclasses import dataclass
from src.decorators import (do_twice, timer, debug, slow_down, register,
                            PLUGINS, login_required, repeat)


app = Flask(__name__)


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


@app.route("/secret")
@login_required
def secret():
    """Render secret page."""
    return "<p>This is a secret page.</p>"


class Circle:
    """Represents a circle."""

    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """Get value of radius."""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Set radius, raise error if negative."""
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive.")

    @property
    def area(self):
        """Calculate area inside circle."""
        return self.pi() * self.radius**2

    def cylinder_volume(self, height):
        """Calculate volume of cylinder with circle as base."""
        return self.area * height

    @classmethod
    def unit_circle(cls):
        """Create a circle with radius 1."""
        return cls(1)

    @staticmethod
    def pi():
        """Vaue of π, could use math.pi instead though."""
        return 3.1415926535


class TimeWaster:
    """A waster of time."""

    @debug
    def __init__(self, max_num):
        self.max_num = max_num

    @timer
    def waste_time(self, num_times):
        """Waste some time."""
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_num)])


@dataclass
class PlayingCard:
    """Represents a playing card."""

    rank: str
    suit: str


@debug
@do_twice
def greet2(name):
    """Greet the caller."""
    print(f"Hello {name}")


@do_twice
@debug
def greet3(name):
    """Greet the caller."""
    print(f"Hello {name}")


@repeat(num_times=4)
def greet4(name):
    """Greet the caller."""
    print(f"Hello {name}")
