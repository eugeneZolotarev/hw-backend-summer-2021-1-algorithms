__all__ = ("is_prime",)

import math


def is_prime(number: int) -> bool:
    """Определяет, является ли число простым.

    Example:
        >> is_prime(0):
        False
        >> is_prime(1):
        False
        >> is_prime(4):
        True
    """
    i = 2
    while (i < number - 1):
        if number % i == 0:
            return False
        i += 1
    return False if number == 0 or number == 1 else True
