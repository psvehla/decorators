from datetime import datetime


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass  # Hush, the neighbours are asleep.
    return wrapper


def say_whee():
    print("Whee!")


say_whee = my_decorator(say_whee)
say_whee = not_during_the_night(say_whee)
