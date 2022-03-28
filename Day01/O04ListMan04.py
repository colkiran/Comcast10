
"""
1. sort     -   will sort the original list
2. sorted   -   will sort the list and returns a copy of it.

3. reverse and reversed

"""

print("sort".center(40, "-"))
l = [10, 5, 9, 1, 8, 2, 4, 7, 3, 5, 6]
print(f"l :{l}")

res = sorted(l)
print(f"asc sorted list :{res}")

res1 = sorted(l, reverse=True)
print(f"desc sorted list :{res1}")

print("-" * 40)
l = [10, 'zebra', 5,'apple', 'orange', 9, 'yellow', 'violet', 1, 'green', 'blue', 8, 'pink',
     2, 'red', 4, 'maroon', 7, 'cat', 'ball', 3, 'kite',  5, 'jam', 6, 1024, 19, 128, 250, 28, 2104,
     33, 302, 3245]
print(f"l :{l}")

print("-" * 40)
res = sorted(l, key=ascii)
print(f"res :{res}")

print("-" * 40)
cities = ['thiruvananthapuram', 'pune', 'bangalore', 'chennai', 'ooty', 'vishakapatnam',
          'hyderabad', 'kanyakumari', 'madurai', 'mysore', 'delhi']
print(f"cities :{cities}")

print("-" * 40)
res = sorted(cities, key=len)
print(f"res :{res}")

print("-" * 40)
months = ['dec', 'oct', 'aug', 'jan', 'nov', 'feb', 'sep', 'apr', 'jul', 'may', 'jun', 'mar']
print(f"months :{months}")

def srtMon(mon):
    from calendar import month_name
    mn = []
    for m in list(month_name):
        mn.append(m[0:3].lower())
    if mon in mn:
        return mn.index(mon)

sorted_months = sorted(months, key=srtMon)
print(f"sorted_months :{sorted_months}")

print("reverse".center(40,  "-"))
l = [10, 5, 9, 1, 8, 2, 4, 7, 3, 5, 6]
print(f"l :{l}")

l.reverse()
print(f"l :{l}")

print("clear".center(40, "-"))
l = [10, 5, 9, 1, 8, 2, 4, 7, 3, 5, 6]
print(f"l :{l}")

l.clear()
print(f"l :{l}")
