
t1 = tuple()
print(f"t1 :{t1}")
print(type(t1))

print("-" * 40)

t2 = (1, 2, 3, 4, 5)
print(f"t2 :{t2}")
print(type(t2))

print("-" * 40)
t3 = tuple(range(10,101,10))
print(f"t3 :{t3}")
print(type(t3))

print("-" * 40)
t4 = 2,
print(f"t4 :{t4}")
print(type(t4))

print("-" * 40)
t5 = 1, 2, 3, 4, 5
print(f"t5 :{t5}")
print(type(t5))

t = ('a', 'b', 'c', 'd')
print(f"t[2] :{t[2]}")
# t[2] = "cat"

print("-" * 40)
# print(dir(t))

print("count".center(40, "-"))
t1 = (1, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 1, 3, 4, 1, 2, 1, 2, 3)
print(f"t1 :{t1}")

print("1 :", t1.count(1))
print("2 :", t1.count(2))
print("3 :", t1.count(3))


print("index".center(40, "-"))
t1 = (1, 1, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1, 1, 3, 4, 1, 2, 1, 2, 3)
print(f"t1 :{t1}")

print("3 :", t1.index(3))
print("4 :", t1.index(3, 7))
print("5 :", t1.index(3, 14))
