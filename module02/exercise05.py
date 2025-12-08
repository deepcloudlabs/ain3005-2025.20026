import json
from collections import defaultdict
from functools import reduce
from itertools import chain


def groupByGenreAndSum(groups, element):
    groups[element[0]] = groups.get(element[0], 0) + element[1]
    return groups


with open("resources/movies.json", "r", encoding="utf-8") as f:
    movies = json.load(f)
    genre_counts = reduce(groupByGenreAndSum, map(lambda genre: (genre["name"], 1),
                                                  chain.from_iterable(map(lambda movie: movie["genres"], movies))),
                          defaultdict(int))
    print(genre_counts)