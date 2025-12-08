n = int(input("n: "))
count = 0
for i in range(1, n + 1):
    if (i%3 == 0 and i%5 != 0) or (i%3 != 0 and i%5 == 0):
        count += 1
ratio = count / n
print(f"Ratio of good numbers: {ratio}")
