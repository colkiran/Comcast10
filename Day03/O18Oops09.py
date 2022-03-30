
class Player:
    def __init__(self,name,runs):
        self.name=name
        self.runs=runs

    def __str__(self):
        return f"Name:{self.name}\nRuns :{self.runs}"

    def __add__(self,other):
        return f"Total runs:{self.runs+other.runs}"

    def __sub__(self, other):
        return f"Total runs:{self.runs - other.runs}"

    def __mul__(self, other):
        return f"Total runs:{self.runs * other.runs}"

    def __truediv__(self, other):
        return f"Total runs:{self.runs / other.runs}"

    def __floordiv__(self, other):
        return f"Total runs:{self.runs // other.runs}"

p1=Player("Rohit",120)
p2=Player("Dhoni",60)

print(p1)
print("-" * 40)
print(p2)

print("-" * 40)
print("Add :", p1 + p2)

print("-" * 40)
print("Subtract :", p1 - p2)

print("-" * 40)
print("Multiply :", p1 * p2)

print("-" * 40)
print("Divide :",p1 / p2)

print("-" * 40)
print("Floor Divide :", p1 // p2)
