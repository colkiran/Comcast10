
s1 = set()
print(f"s1 :{s1}")
print(type(s1))

print("-" * 40)
s2 = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
print(f"s2 :{s2}")
print(type(s2))

print("-" * 40)
s3 = {1, 2, 3, 'four', 'five', 'six', 7.9, 8.2, 'nine', True, False, 3+5j}
print(f"s3 :{s3}")

print("-" * 40)
s4 = set(range(1, 11))
print(f"s4 :{s4}")

for i in s4:
    print(i, end=" ")
print()

print("-" * 40)
s5 = {1, 2, 3}

s5.add(1)
s5.add(3)
s5.add(4)
s5.add(2)
s5.add(5)
print(f"s5 :{s5}")

s5.update([1, 2, 3])
s5.update([3, 4, 5])
s5.update([5, 6, 7])
print(f"s5 :{s5}")

res = s5.pop()
print(f"res :{res}")
res = s5.pop()
print(f"res :{res}")
print(f"s5 :{s5}")

s5.remove(5)
s5.remove(7)
print(f"s5 :{s5}")

s5.discard(4)
s5.discard(1)
print(f"s5 :{s5}")

print("-" * 40)
A = {1, 2, 3, 4, 5, 6}
B = {5, 6, 7, 8, 9, 10}

print(f"A :{A}")
print(f"B :{B}")

print("A union B :", A | B)
print("B union A :", B.union(A))

print("-" * 40)
print("A intersection B :", A & B)
print("B intersection A :", B.intersection(A))

print("-" * 40)
print("A difference B :", A - B)
print("B difference A :", B.difference(A))

print("-" * 40)
print("A symmetric difference B :", A ^ B)
print("B symmetric difference A :", B.symmetric_difference(A))

# frozen set - are immutable
print("-" * 40)
x = frozenset([1, 2, 3, 4, 5])
print(f"x :{x}")
