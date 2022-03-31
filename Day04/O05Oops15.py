
class Product:

    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return f"The price of the product is :{self.__price}"

    def set_price(self, prc):
        self.__price = prc

    def del_price(self):
        self.__price = 0

    price = property(get_price, set_price, del_price)

fanta = Product(45)
print(fanta.price)

fanta.price = 65
print(fanta.price)

del fanta.price
print(fanta.price)

fanta.price = 80
print(fanta.price)
