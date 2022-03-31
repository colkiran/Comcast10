
class Employee:

    def __init__(self, name):
        self.__name = name              # private variable
        self.tech = ['java', 'j2ee', 'spring', 'hibernate', 'C++', 'AngularJS']

    def __str__(self):
        return "Name : " + self.__name + "\nTech :" + ", ".join([v for v in self.tech])


emp1 = Employee("Jack")
print(emp1)

# print(emp1.__name)
print(emp1.__dict__)
print("-" * 40)
emp1._Employee__name = "Jill"
print(emp1)
