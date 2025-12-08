import json
from collections import defaultdict
from functools import reduce
_70s = lambda movie: 1970 <= movie["year"] < 1980
is_drama = lambda movie : any(genre["name"] == "Drama" for genre in movie["genres"])
# movies in 70s and in Drama
with open("resources/movies.json","r",encoding="utf-8") as f:
    movies = json.load(f)
    drama_movies_in_70s = sorted(filter(_70s,filter(is_drama,movies)),key=lambda movie: movie["year"],reverse=True)
    for movie in drama_movies_in_70s:
        print(movie)