
class Animal:

    def __init__(self):
        print("Animal Ctor....")
        self.a = 10

    def eat(self):
        print("Animals eat....")

    def fun(self):
        print("Function fun of Animal class....")

class Person:

    def __init__(self):
        print("Person Ctor....")
        self.p = 20

    def talk(self):
        print("Person talks...")

    def fun(self):
        print("Function fun of Person class....")

class Girl(Animal, Person):

    def __init__(self):
        super().__init__()
        Person.__init__(self)
        print("Girl Ctor....")
        self.g = 30


grace = Girl()

print("-" * 40)
grace.eat()
grace.talk()

print("-" * 40)
grace.fun()                 # => which fun will it call and why

print("-" * 40)
print(grace.__dict__)