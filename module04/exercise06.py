import json

with open("resources/employees.json", mode="rt") as file:
    employees = json.load(file)
    for employee in employees:
        print(employee)