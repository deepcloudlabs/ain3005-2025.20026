from itertools import islice

# use the elements without acquiring memory
dataset = []
first_10k = list(islice(dataset, 10_000))
