import employees_pb2

# create employee object
employee1 = employees_pb2.Employee()
employee1.id = 1001
employee1.name = 'employee 1'
employee1.salary = 9000000

# create employee object
employee2 = employees_pb2.Employee()
employee2.id = 1002
employee2.name = 'employee 2'
employee2.salary = 7000000

# create employee object
employee3 = employees_pb2.Employee()
employee3.id = 1003
employee3.name = 'employee 3'
employee3.salary = 8500000

# print(employee1.id)
# print(employee2.name)
# print(employee3.salary)

# append employee object to employees
emps = employees_pb2.Employees()
emps.employees.append(employee1)
emps.employees.append(employee2)
emps.employees.append(employee3)

print(emps)