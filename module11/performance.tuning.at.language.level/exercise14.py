import time
import random


def create_heavy_dataset(size):
    """
    Bottleneck 1: Inefficient String Concatenation.
    Strings are immutable in Python. Using += in a loop creates a new
    string object every single iteration.
    """
    print(f"Generating dataset with {size} items...")
    dataset = []
    for _ in range(size):
        # BAD: Using += for string building in a loop
        s = ""
        for j in range(10):
            s += str(random.randint(0, 9))
        dataset.append(s)
    return dataset


def slow_search(dataset, find_me):
    """
    Bottleneck 2: Algorithmic Complexity (O(N) lookup).
    We are searching a list repeatedly. A Set would be O(1).
    """
    print("Starting search...")
    matches = 0
    for item in find_me:
        if item in dataset:
            matches += 1
    return matches


def simulate_database_call():
    """
    Bottleneck 3: I/O Bound.
    This simulates waiting for a network response or disk read.
    """
    print("Querying database...")
    time.sleep(2)  # The CPU is doing nothing here, but time is passing.
    return [str(random.randint(0, 9999999999)).zfill(10) for _ in range(500)]


def main():
    # 1. CPU Bound: Inefficient string creation
    data = create_heavy_dataset(500_000)

    # 2. I/O Bound: Simulating a slow DB call
    search_targets = simulate_database_call()

    # 3. CPU Bound: Inefficient Search
    hits = slow_search(data, search_targets)

    print(f"Found {hits} matches.")


if __name__ == "__main__":
    main()
