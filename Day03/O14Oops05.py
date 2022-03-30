
class Player:
    team = "India"

    def __init__(self, name, age):
        self.name = name
        self.age = age

        # self will have the name of the object that called the method
    def get_details(self):
        print(f"Name :{self.name} \nAge :{self.age}")

ply1 = Player("Sachin", 36)
ply1.get_details()

print("-" * 40)
ply2 = Player("Rohit", 30)
ply2.get_details()

print("-" * 40)
print(f"Player :{Player.team}")
print(f"ply1 :{ply1.team}")
print(f"ply2 :{ply2.team}")

print("-" * 40)
Player.team = "RCB"
print(f"Player :{Player.team}")
print(f"ply1 :{ply1.team}")
print(f"ply2 :{ply2.team}")

print("-" * 40)
ply2.team = "MI"
print(f"ply2 :{ply2.team}")
print(f"Player :{Player.team}")
print(f"ply1 :{ply1.team}")

print("-" * 40)
print(ply2.__dict__)
