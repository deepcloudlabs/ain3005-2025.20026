data_set = [1,2,3,4,5] # 1M
# it is a bad idea to create another collection
# increased memory footprint -> GC
total = sum([x*x for x in data_set])

# better: generator function: memory footprint
total = sum(x*x for x in data_set)


