import math


def gun(x: float) -> float:
    return x ** 2

def fun(x: float) -> float:
    return gun(x) + 3 * x + 5


xs = list(range(0, 1_000_000))  # assume xs is a LARGE list > 1M elements

for i in xs:
    # y = fun(i)
    y = i * i + 3 * i + 5 # inlining

math.fsum(xs)