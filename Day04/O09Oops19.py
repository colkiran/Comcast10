
class Animal:

    def eat(self):
        print("Animals eat...")

class Bird(Animal):

    def fly(self):
        print("Birds fly....")

class Chicken(Bird):

    def fly(self):
        print("Chickens fly only for a shoter distance...")

chick = Chicken()
chick.eat()
chick.fly()
