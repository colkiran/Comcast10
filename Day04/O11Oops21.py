
from abc import ABC,abstractmethod

class Account(ABC):

    def __init__(self):
        print("Account.....")

    def minBalance(self):
        pass

    @abstractmethod
    def getBalance(self):
        pass

class Savings(Account):

    def deposit(self, amt):
        print(f"{amt} credited into the account successfully....")

    def getBalance(self):
        print("Balance in the accout is #####.##")

sa = Savings()
sa.getBalance()
