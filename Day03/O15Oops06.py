
class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        # self will have the name of the object that called the method
    def get_details(self):
        print(f"Name :{self.name} \nAge :{self.age}")

    @classmethod
    def CreatePlayer(cls, fname, lname, age):
        # factory
        return cls(f"Mr. {fname} {lname}", age)             # pass


ply1 = Player("Virat", 34)
ply1.get_details()

print("-" * 40)
ply2 = Player.CreatePlayer("Sachin", "Tendulkar", 36)
ply2.get_details()
