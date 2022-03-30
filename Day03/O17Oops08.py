
class Employee:
    def __init__(self, name, sal):
        self.name = name
        self.sal = sal

        # self will have the name of the object that called the method
    def __str__(self):
        return f"Name :{self.name} \nSalary :{self.sal}"

    def __eq__(self, other):
        return self.sal == other.sal

    def __gt__(self, other):
        return self.sal > other.sal

emp1 = Employee("Mike", 75000)
print(emp1)

print("-" * 40)
emp2 = Employee("David", 65000)
print(emp2)

print("-" * 40)
# print(emp1 == emp2)             # comparing the addresses by default

if (emp1 == emp2):
    print("{}'s salary of {} is equal to {}'s salary of {}".format(emp1.name, emp1.sal,
                                                                   emp2.name, emp2.sal))
else:
    print("{}'s salary of {} is NOT equal to {}'s salary of {}".format(emp1.name, emp1.sal,
                                                                   emp2.name, emp2.sal))

print("-" * 40)

if (emp1 != emp2):
    print("{}'s salary of {} is NOT equal to {}'s salary of {}".format(emp1.name, emp1.sal,
                                                                   emp2.name, emp2.sal))
else:
    print("{}'s salary of {} is equal to {}'s salary of {}".format(emp1.name, emp1.sal,
                                                                   emp2.name, emp2.sal))
print("-" * 40)

if (emp1 > emp2):
    print("{}'s salary of {} is Greater Than {}'s salary of {}".format(emp1.name, emp1.sal,
                                                                   emp2.name, emp2.sal))
else:
    print("{}'s salary of {} is NOT Greater Than {}'s salary of {}".format(emp1.name, emp1.sal,
                                                                   emp2.name, emp2.sal))
print("-" * 40)

if (emp1 < emp2):
    print("{}'s salary of {} is Less Than {}'s salary of {}".format(emp1.name, emp1.sal,
                                                                   emp2.name, emp2.sal))
else:
    print("{}'s salary of {} is NOT Less Than {}'s salary of {}".format(emp1.name, emp1.sal,
                                                                   emp2.name, emp2.sal))
