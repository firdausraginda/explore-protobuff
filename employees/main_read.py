import employees_pb2

emps = employees_pb2.Employees()

# parse message from given binary file ---------------------------------------------------------------
f = open('./employees/employees_binary', "rb") # "rb" means open a file for reading only in binary format
emps.ParseFromString(f.read())
f.close()

# loop binary file ---------------------------------------------------------------
list_employees = []

for emp in emps.employees:

    emp_dict = {}
    emp_dict['id'] = emp.id
    emp_dict['name'] = emp.name
    emp_dict['salary'] = emp.salary
    
    list_employees.append(emp_dict)

print(list_employees)
print(list_employees[0])