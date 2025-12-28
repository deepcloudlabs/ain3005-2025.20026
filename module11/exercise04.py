with open('largefile.txt', 'w') as f:
    while True:
        f.write('a' * 10_000_000)
