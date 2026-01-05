data_set = [{"x": 0,"y": 0, "radius": 0 },]
sum(circle["radius"] for circle in data_set)
any(circle["radius"] == 0 for circle in data_set)
# all()
# min()
max(data_set, key=lambda x: x["radius"] )
# sorted()