
print("count".center(40, "-"))
l1 = [1, 2, 1 ,3, 1, 1, 2, 1, 2, 3, 1, 1, 2, 2, 1, 4, 3, 1, 2, 1, 1, 1, 1, 1]
print(f"l1 :{l1}")
print("1 :", l1.count(1))
print("2 :", l1.count(2))
print("3 :", l1.count(3))
print("8 :", l1.count(8))

print("index".center(40, "-"))
l1 = [1, 2, 1 ,3, 1, 1, 2, 1, 2, 3, 1, 1, 2, 2, 1, 4, 1, 2, 1, 1, 1, 3, 1, 1]
print(f"l1 :{l1}")
print(f"l1.index(3) :{l1.index(3)}")
print(f"l1.index(3) :{l1.index(3, 4)}")
print(f"l1.index(3) :{l1.index(3, 10)}")
# print(f"l1.index(8) :{l1.index(8)}")

print("copy".center(40, "-"))
l1= [1, 2, 3, 4, 5]
print(f"l1 Before :{l1}")
l2 = l1                     # shallow copy - not copies the values but also copies the addresses
print(f"l2 Before :{l2}")

print("-" * 40)
l2.extend([6, 7, 8])
print(f"l2 After :{l2}")
print(f"l1 After :{l1}")

print("-" * 40)
l3 = [10, 20, 30, 40, 50]
print(f"l3 Before :{l3}")
l4 = l3.copy()                  # deep copy - copies only the values not the addresses
print(f"l4 Before :{l4}")

print("-" * 40)
l4.insert(1, 15)
l4.insert(3, 25)
l4.insert(5, 25)
print(f"l4 After :{l4}")
print(f"l3 After :{l3}")

print("-" * 40)
l5 = [1, 2, 3, 4, [5, 10, 15, 20, 25], 5]
print(f"l5 Before :{l5}")
l6 = l5.copy()
print(f"l6 Before :{l6}")

print("-" * 40)
l6[4].extend([30, 35, 40])
print(f"l6 After :{l6}")
print(f"l5 After :{l5}")

print("-" * 40)
from copy import deepcopy
l7 = [1, 2, 3, [2, 4, 6, 8, 10], 4, 5]
print(f"l7 Before :{l7}")
l8 = deepcopy(l7)
print(f"l8 Before :{l8}")

print("-" * 40)
l8[3].extend([12, 14, 16])
print(f"l8 After :{l8}")
print(f"l7 After :{l7}")
