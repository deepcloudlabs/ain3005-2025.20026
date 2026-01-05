import re
from re import fullmatch

name1 = "jack bauer"
name2 = "jack bauer"

name1.upper()
def fun():
    s = "a" * 1_000
    for i in range(0,1_000_000):
        re.match("^[0-9]{4}-[0-9]{3}$", s)

def gun():
    pattern = re.compile("^[0-9]{4}-[0-9]{3}$")
    s = "a" * 1_000
    for i in range(0,1_000_000):
        pattern.match(s)

fun()
gun()