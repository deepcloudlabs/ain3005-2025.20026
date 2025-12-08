from threading import Thread

data = 0

def fun(n):
    global data
    total = 0
    for i in range(n):
        total += 1
    data = total

print(data)
thread = Thread(target=fun, args=(10_000_000,))
thread.start()
thread.join()
print(data)