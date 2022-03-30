
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.sal = salary
        self.tech = ['C#', 'asp.net', 'Javascript', 'HTML 5', 'CSS', 'Angular', 'React']

    def __str__(self):
        return "{} and {}".format(self.name, self.sal)

    def __len__(self):
        return len(self.tech)

    def __iter__(self):
        return iter(self.tech)

emp1 = Employee("Kevin", 35000)
print(emp1)

print("-" * 40)
print(len(emp1))

print("-" * 40)
print([tech for tech in emp1])
