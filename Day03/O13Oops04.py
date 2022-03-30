
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # self will have the name of the object that called the method
    def get_details(self):
        print(f"Name :{self.name} \nAge :{self.age}")

ply1 = Player("Sachin", 34)
ply1.get_details()

ply2 = Player("Rahul", 30)
ply2.get_details()
print("-" * 40)

print(ply1.__dict__)
print(ply2.__dict__)
ply2.runs = 145

print(ply1.__dict__)
print(ply2.__dict__)
