import json
from functools import reduce
def get_population(country):
    return country["population"]
# imperative approach
with open("resources/countries.json",encoding="utf-8") as file:
    countries = json.load(file)
    if_asian = lambda country : country["continent"] == "Asia"
    to_population = lambda country : country["population"]
    to_sum = lambda x,y: x + y
    #total_population = reduce(to_sum,map(get_population,filter(if_asian,countries)),0)
    total_population = reduce(lambda x,y: x+y,map(lambda country: country["population"],filter(lambda country: country["continent"] == "Asia",countries)),0)
    print(f"Total population: {total_population}")
