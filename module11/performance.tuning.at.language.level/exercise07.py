from dataclasses import dataclass


class Point:
    __slots__ = ("x", "y")
    def __init__(self, x, y):
        self.x = x
        self.y = y

# 10M
"""
memory footprint
speed up attribute access   
"""

# since 3.10+
@dataclass(slots=True)
class Point2D:
    x: float
    y: float