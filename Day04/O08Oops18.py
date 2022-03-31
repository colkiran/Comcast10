
class Animal:

    def __init__(self):
        print("Animal Ctor...")
        self.age = 1

    def eat(self):
        print("Animals eat...")


class Bird(Animal):

    def __init__(self):
        super().__init__()
        print("Bird Ctor...")
        self.weight = '1k'

    def fly(self):
        print("Birds fly....")

cuckoo = Bird()
print(cuckoo.__dict__)
cuckoo.eat()
cuckoo.fly()
print(cuckoo.age)
print(cuckoo.weight)

