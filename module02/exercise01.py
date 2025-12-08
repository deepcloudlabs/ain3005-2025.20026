import json
# imperative approach
with open("resources/countries.json",encoding="utf-8") as file:
    countries = json.load(file)
    total_population = 0
    for country in countries:
        if country["continent"] == "Asia":
            population = country["population"]
            total_population += population
    print(f"Total population: {total_population}")
