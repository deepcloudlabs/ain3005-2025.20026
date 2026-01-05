import threading
x = 0

def worker():
    global x
    while True:
        x = x + 1

for _ in range(100):  # Spawns too many threads
    threading.Thread(target=worker).start()
