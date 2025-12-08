numbers = [4, 8, 15, 16, 23, 42]


def odd(number):
    print(f"inside odd: {number}")
    return number % 2 == 1


def bau_filter(filter_fun, items):
    print("bau_filter is just started")
    for item in items:
        if filter_fun(item):
            yield item
    print("bau_filter is just completed")

def bau_map(map_fun,items):
    print("bau_map is just started")
    for item in items:
        yield map_fun(item)

tripled_odds = bau_map(lambda x: x ** 3, bau_filter(odd, numbers))
for odd in tripled_odds:
    print(odd)