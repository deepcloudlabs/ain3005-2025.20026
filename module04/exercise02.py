employees = []
with open("resources/employees.txt",mode="rt") as file:
    for line in file:
        full_name, department, salary, birth_year, full_time = line.split(",")
        employees.append((full_name,department,salary,birth_year,full_time))
for full_name, department, salary, birth_year, full_time in employees:
    print(f"{full_name},{department},{salary},{birth_year},{full_time}")
