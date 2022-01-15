import employees_pb2

# singular message field ---------------------------------------------------------------
employee1 = employees_pb2.Employee()
employee1.id = 1001
employee1.name = 'employee 1'
employee1.salary = 9000000

employee2 = employees_pb2.Employee()
employee2.id = 1002
employee2.name = 'employee 2'
employee2.salary = 7000000

employee3 = employees_pb2.Employee()
employee3.id = 1003
employee3.name = 'employee 3'
employee3.salary = 8500000

# print(employee1.id)
# print(employee2.name)
# print(employee3.salary)

# repeated message fields using `add()` ---------------------------------------------------------------
emps_add = employees_pb2.Employees()
emps_add.employees.add(id=2001, name='employee 11', salary=4000000)
emps_add.employees.add(id=2002, name='employee 12', salary=4500000)
emps_add.employees.add(id=2003, name='employee 13', salary=6000000)

# print(emps_add)

# repeated message fields using `append()` ---------------------------------------------------------------
emps_append = employees_pb2.Employees()
emps_append.employees.append(employee1)
emps_append.employees.append(employee2)
emps_append.employees.append(employee3)

# print(emps_append)

# serialize message ---------------------------------------------------------------
f = open('employees_binary', "wb") # "wb" means overwrite a file in binary format
f.write(emps_append.SerializeToString())
f.close()