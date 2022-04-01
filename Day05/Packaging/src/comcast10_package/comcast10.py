
gname = "Rahul Dravid"

runs = {'test': 15800, 'odis': 18000, 't20': 1500}

sports = ['cricket', 'hockey', 'soccer', 'tennis', 'swimming']

# ----------------------------------------------------

def greet(gname):
    print(f"Greetings {gname}, Welcome to the event")

def addMe(x, y):
    return x + y

# ----------------------------------------------------
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name is :{self.name}\nAge is {self.age}")

