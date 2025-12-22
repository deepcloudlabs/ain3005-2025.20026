import employee_pb2

employees_msg = employee_pb2.Employees()
with open("resources/employees.bin", "rb") as f:
    employees_msg.ParseFromString(f.read())

for emp in employees_msg.employees:
    print(f"Name: {emp.name}, Dept: {emp.department}, "
          f"Salary: {emp.salary}, Birth Year: {emp.birth_year}, "
          f"Full-time: {emp.full_time}")