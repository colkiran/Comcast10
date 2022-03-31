
class Product:

    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        print("Price Getter")
        return f"The price of the product is :{self.__price}"

    @price.setter
    def price(self, prc):
        print("Price Setter")
        self.__price = prc

    @price.deleter
    def price(self):
        print("Price Deleter")
        self.__price = 0

sprite = Product(120)
print(sprite.price)

sprite.price = 90
print(sprite.price)

del sprite.price
print(sprite.price)

sprite.price = 75
print(sprite.price)
