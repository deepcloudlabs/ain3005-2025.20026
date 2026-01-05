data_set = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # 10M

out1 = [{"x": x, "y": x * x} for x in data_set]

# better
out2 = [(x, x*x) for x in data_set]