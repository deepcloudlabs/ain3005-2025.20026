import pickle


with open("resources/employees.pkl", mode='rb') as file:
    employees = pickle.load(file)
    for employee in employees:
        print(employee)