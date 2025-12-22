n = 1_000_234_567

with open("resources/out.bin", "wb") as f:
    f.write(n.to_bytes(4, byteorder="big", signed=False))  # 4-byte unsigned

with open("resources/out.bin", "rb") as f:
    data = f.read(4)  # read exactly 4 bytes
    n = int.from_bytes(data, byteorder="big", signed=False)

print(n)
with open("resources/out.txt", "wt") as f:
    f.write(f"{n}")