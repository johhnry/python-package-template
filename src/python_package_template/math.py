from typing import Callable


def add(a: float, b: float) -> float:
    return a + b


FnFloat = Callable[[float, float], float]


def apply(f: FnFloat, a: float, b: float) -> float:
    return f(a, b)


def mult(a: float, b: float) -> float:
    return a * b
