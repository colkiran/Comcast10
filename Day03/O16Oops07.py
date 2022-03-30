
# Magic Methods
class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        # self will have the name of the object that called the method
    def __str__(self):
        return f"Name :{self.name} \nAge :{self.age}"

ply1 = Player("Dhoni", 37)
print(str(ply1))

print("-" * 40)
print(ply1)             # implicitly calls __str__

print("-" * 40)
a = 10
print(f"a :{a}")
print(type(a))

b = str(a)
print(f"b :{b}")
print(type(b))
