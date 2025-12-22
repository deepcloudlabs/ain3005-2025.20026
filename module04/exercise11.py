# write_employees.py
import employee_pb2

employees = [
    ("jack shephard", "Sales", 100000, 1978, True),
    ("kate austen", "IT", 200000, 1985, False),
    ("ben linus", "Finance", 150000, 1967, True),
    ("james sawyer", "HR", 70000, 1979, True),
    ("kim kwon", "Sales", 120000, 1986, True),
    ("sun kwon", "IT", 170000, 1984, False),
    ("hugo reyes", "IT", 120000, 1992, True)
]

employees_msg = employee_pb2.Employees()

for name, dept, salary, birth_year, full_time in employees:
    emp = employees_msg.employees.add()
    emp.name = name
    emp.department = dept
    emp.salary = salary
    emp.birth_year = birth_year
    emp.full_time = full_time

with open("resources/employees.bin", "wb") as f:
    f.write(employees_msg.SerializeToString())