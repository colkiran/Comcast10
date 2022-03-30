
class Player:               # pascal casing

    def get_runs(self):
        print(self.__class__)
        print("Runs scored.....")

sachin = Player()
sachin.get_runs()
print(type(sachin))

print("-" * 40)
print(isinstance(sachin, Player))
print(isinstance(sachin, object))
print(isinstance(sachin, str))
