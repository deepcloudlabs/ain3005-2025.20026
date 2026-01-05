import threading

def compute():
    while True:
        sum([i ** 2 for i in range(10_000)])

for _ in range(4):  # Spawns multiple threads
    threading.Thread(target=compute).start()

