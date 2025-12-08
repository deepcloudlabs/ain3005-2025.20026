import time
from threading import Thread

# Shared resource (not protected by any lock - intentionally thread-unsafe)
data = 0


def increment(counter):
    global data
    for _ in range(counter):
        temp = data
        time.sleep(0)
        data = temp + 1

print(f"Initial value of data: {data}")

threads = []
num_threads = 10
increments_per_thread = 100_000

for _ in range(num_threads):
    thread = Thread(target=increment, args=(increments_per_thread,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"Final value of data (thread-unsafe): {data}")