"""
return -> solution
yield -> generator function -> yields partial solutions
raise -> an exception
"""
d = dict()
k = "TUR"
try:
    country = d[k]
except KeyError:
    country = None

country = d.get(k, None)
