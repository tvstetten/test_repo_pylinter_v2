import math
import os


def add(a, b) -> int:
    # OK
    return math.floor(a + b)


def to_sentence(s) -> str:
    s = s.capitalize()

    if s.endswith('.'):
        return s
    else:
        return s + '.'
