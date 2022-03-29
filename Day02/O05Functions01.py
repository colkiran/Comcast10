
def greet():
    print("Greetings Mr. Sachin, Welcome to the event....")

def greetGst(gname):
    print(f"Greetings Mr. {gname}, Welcome to the event....")

# there are two args the function takes one is gname which is a non default arg
# the second one is city and its a default arg
def greetGstCity(gname, city = "Mumbai"):
    print(f"Greetings Mr. {gname} from {city}, Welcome to the event....")


greet()

print("-" * 40)
greetGst("Mike Tyson")

print("-" * 40)
greetGstCity("Sachin")
greetGstCity("Rohit")
greetGstCity("Ashwin", "Chennai")       # overwriting the value of city

print("-" * 40)
# named args
def admisn(fname, lname, dob, qlf, cnum, addr, city):
    print(f"fname :{fname}")
    print(f"lname :{lname}")
    print(f"dob :{dob}")
    print(f"qlf:{qlf}")
    print(f"cnum :{cnum}")
    print(f"addr :{addr}")
    print(f"city :{city}")

admisn(dob="23/10/1962", qlf="Degree", fname="Micheal", lname="Jordan", addr="8th lane, first cross",
       city="Newyork", cnum=34283004)

print("-" * 40)
# function can return a value
def Add_me(x, y):
    return x + y

print("The sum of {} and {} is {}".format(234, 345, Add_me(234, 345)))

def arith_Calc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    return sum, diff, prod, quot

# the function will return all arguments and will be stored in a tuple
res = arith_Calc(20, 8)
print(f"res :{res}")

# factorial of a number, fibanocci series using recursive calls

# variable length arguments
# *arg, **kwargs

# if a variable is prefixed with * then we can pass args like a tuple
print("-" * 40)
def prodAll(*num):
    print(f"num :{num}")
    print("num :", *num)               # unpacking the tuple
    prod = 1
    for i in num:
        prod *= i
    return prod

print("Multiply All :", prodAll(1, 2, 3, 4, 5, 6, 7))

print("-" * 40)
def extractDetails(**details):
    print(details)
    # print(**details)
    print("Name :", details['name'])

extractDetails(name="Sachin", runs=123, oppn="SA")

print("-" * 40)
def plrDetails(pname, *sports, **runs):
    print("Name :", pname)
    print("Fav sports :", sports)
    print("Runs scored :", runs)

plrDetails("Rahul Dravid", 'cricket', 'soccer', 'hockey', 'tennis', odi=18500, tests=13200, t20=1850)

print("-" * 40)

def fun():
    "The quick brown fox jumps over the lazy dog"
    # this is a comment
    print("hello world")

fun()
print(fun.__doc__)              # doc string

print("-" * 40)

def fun1(arg1, arg2):
    """
    function fun1 takes two args
        a. arg1
        b. arg2
    if we pass both arguments as numbers then we get the sum of two numbers
        30 = fun1(10, 20)

    if we pass both arguments as string then we get a concatenated string
        helloworld = fun1("hello", "world")

    else it will throw an error message
        error = fun1("hello", 30)
    """
    return arg2 + arg1

res = fun1(234, 645)
print(f"res :{res}")

res1 = fun1("hello", "world")
print(f"res1 :{res1}")

print("=*" * 40)
print("=*" * 40)

help(fun1)
