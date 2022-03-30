
def sum(x, y):
    print("sum function called....")
    return f"The sum of {x} and {y} is :{x + y}"

def diff(x, y):
    print("diff function called....")
    return f"The difference of {x} and {y} is :{x - y}"

def prod(x, y):
    print("prod function called....")
    return f"The product of {x} and {y} is :{x * y}"


def outerFun(fnc):                      # HOF

    def innerFun(*args):
        print("login to the service....")
        print(fnc(*args))
        print("logout of the service.....")
        print("-" * 40)

    return innerFun

sumRef = outerFun(sum)
diffRef = outerFun(diff)
prodRef = outerFun(prod)

sumRef(20, 40)

diffRef(80, 50)

prodRef(30, 6)
