
"""
lambdas -
anonymous functions - functions without names
with a single expression - funtion with a single expression

lambda var1, var1.....: expression
the result of the expression will be the return value of lambda

lambdas are used with
a. map
b. filter
c. reduce

"""

def add(x, y):
    return x + y

a = add
res = a(20, 50)
print(f"res :{res}")

print("-" * 40)

b = lambda x, y : x + y

res = b(56, 76)
print(f"res :{res}")

print("map".center(40, "-"))
l = list(range(1, 11))
print(f"l :{l}")

res = list(map(lambda x: x ** 2, l))
print(f"res :{res}")

print("-" * 40)
# filter - expression should return a true or a false
l = list(range(1, 25))
print(f"l :{l}")

res = list(filter(lambda x: x % 3 == 0, l))
print(f"res :{res}")

# reduce => it will reduce the list into a single value
from functools import reduce
l = [8, 10, 24, 20, 18, 15, 3, 12, 25, 19, 22]
print(f"l :{l}")

res = reduce(lambda x, y: x + y, l)
print(f"res :{res}")

print("-" * 40)
res = reduce(lambda x, y: x if x > y else y, l)
print(f"res :{res}")

print("-" * 40)
from calendar import month_name
months = ['dec', 'oct', 'aug', 'jan', 'nov', 'feb', 'sep', 'apr', 'jul', 'may', 'jun', 'mar']
print(f"months :{months}")


# def srtMon(mon):
#     from calendar import month_name
#     mn = []
#     for m in list(month_name):
#         mn.append(m[0:3].lower())
#     if mon in mn:
#         return mn.index(mon)
#
# sorted_months = sorted(months, key=srtMon)

sorted_months = sorted(months, key= list(map(lambda x : x.lower()[0:3], list(month_name))).index)
print(f"sorted_months :{sorted_months}")

# comprehensions -> iterating through a collection (list, dictionary) using lambda syntaxes
