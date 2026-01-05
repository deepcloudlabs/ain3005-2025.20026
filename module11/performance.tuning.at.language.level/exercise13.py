import re
import time
from re import fullmatch

name1 = "jack bauer"
name2 = "jack bauer"

name1.upper()
def fun():
    t0 = time.perf_counter()
    s = "a" * 1_000
    for i in range(0,1_000_000):
        re.match("^[0-9]{4}-[0-9]{3}$", s)
    print("fun: ",time.perf_counter() - t0)

def gun():
    t0 = time.perf_counter()
    pattern = re.compile("^[0-9]{4}-[0-9]{3}$")
    s = "a" * 1_000
    for i in range(0,1_000_000):
        pattern.match(s)
    print("gun: ",time.perf_counter() - t0)

fun()
gun()