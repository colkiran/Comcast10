
class Employee:
    pass


emp1 = Employee()
emp1.name = "Jack"
emp1.age = 28
emp1.sal = 45000

emp2 = Employee()
emp2.name = "Jill"
emp2.age = 27
emp2.sal = 40000

print("-" * 40)
print(f"Name   :{emp1.name}")
print(f"Age    :{emp1.age}")
print(f"Salary :{emp1.sal}")

print("-" * 40)
print(f"Name   :{emp2.name}")
print(f"Age    :{emp2.age}")
print(f"Salary :{emp2.sal}")
