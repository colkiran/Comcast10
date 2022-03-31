
class Employee:

    def __init__(self):
        print("Employee Ctor.....")
        self._dept = "Finance"          # protected varaible
        self.__location = "Mumbai"      # private variable


class Developer(Employee):

    def __str__(self):
        return self._dept
        # print(self.__location)

David = Developer()
print(David)
