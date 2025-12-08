from threading import Thread

data = 0

def fun(n):
    global data
    for i in range(n):
        data += 1

print(data)
threads = []
for i in range(200):
    threads.append(Thread(target=fun, args=(10_000_000,)))
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print(data)