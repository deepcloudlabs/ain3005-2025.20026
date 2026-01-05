parts = ""
chunks = ["a", "b", "c"]
for chunk in chunks:
    parts += "," + chunk


def gun(s: str) -> str:
    # apply certain logic and generates another string
    return s


def sun(items):
    for item in items:
        yield gun(item)


chunks = ["a", "b", "c"]
result = ",".join(sun(chunks))
print(result)


with open("result.txt", "wt") as file:
    for item in sun(chunks):
        file.write(f"{item},")
