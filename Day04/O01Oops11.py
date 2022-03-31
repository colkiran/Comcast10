
class Employee:

    def __init__(self, name):
        self.name = name
        self.tech = ['java', 'j2ee', 'spring', 'hibernate', 'C++', 'AngularJS']

    def __iter__(self):
        return iter(self.tech)

    def __len__(self):
        return len(self.tech)

    def append(self, val):
        self.tech.append(val)

    def __getitem__(self, index):
        return  self.tech[index]

    def __setitem__(self, index, value):
        self.tech[index] = value

emp1 = Employee("James")
print([tech for tech in emp1])

print("-" * 40)
emp1.append('ReactJS')
print([tech for tech in emp1])

print("-" * 40)
x = emp1[0]
print(f"x :{x}")

print("-" * 40)
emp1[4] = 'Jquery'
print([tech for tech in emp1])

