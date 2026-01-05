def fast_sum(items: list[int]):
    acc = 0
    add = int.__add__
    for item in items:
        # acc += item
        # acc = acc + item
        # acc = int.__add__(acc,item)
        acc = add(acc, item)
    return acc

def gun(): # 10% 100x -> 10x
    pass

def fun(items_from, items_to, predicate_fun):
    append = items_from.append
    for item in items_from: # hot loops/spot
        if predicate_fun(item):
            # items_to.append(item) # lookup
            append(item)
