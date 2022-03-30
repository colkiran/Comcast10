
class Player:

    def __init__(self):                 # constructor
        self.name = "Sachin"
        self.age = 36

    def get_details(self):
        print(f"Name :{self.name} \nAge :{self.age}")

    def __del__(self):
        print("Object deleted......")

ply1 = Player()
ply1.get_details()

del ply1

print("-" * 40)
ply2 = Player()
ply2.name = "Rahul"
ply2.age = 32
ply2.get_details()
