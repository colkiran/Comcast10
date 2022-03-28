
l1 = list()
print(f"l1 :{l1}")
print(type(l1))                 # RTTI  Runtime type identification

print("-" * 40)
l2 = [1, 2, 3, 4, 5]
print(f"l2 :{l2}")              # f string used for formatting, interpolation
print(type(l2))

print("-" * 40)
l3 = list(range(1, 11))
print(f"l3 :{l3}")
print(type(l3))

print("-" * 40)
l4 = [1, 2, 3, 4, 5, 6.3, 7.9, 8.5, 'nine', 'ten', 'eleven', 12 + 1j, 13-0j, True, False]
print(f"l4 :{l4}")
print(type(l4))

# address of a variable or element
# lists can be indexed

print(f"l4[0] :{l4[0]}")
print(f"l4[8] :{l4[8]}")

print("-" * 40)
print(id(l4[0]))                # address of element l4[0]
print(id(l4[1]))                # address of element l4[1]
print(id(l4[2]))                # address of element l4[2]
print(id(l4[4]))
print(id(l4[5]))
print(id(l4[7]))
print(id(l4[8]))

print("-" * 40)
l5 = list(range(1, 11))
print(f"l5 :{l5}")

print(l5[0])
print(l5[5])
print(l5[9])

print("-" * 40)
# reverse index
print(l5[-1])
print(l5[-5])
print(l5[-10])

# slicing  - part of an array
print(f"l5 :{l5}")
print(f"l5[0:6] :{l5[0:6]}")
print(f"l5[6:11] :{l5[6:11]}")
print(f"l5[0:11:2] :{l5[0:11:2]}")
print(f"l5[0:]  :{l5[0:]}")
print(f"l5[:11] :{l5[:11]}")
print(f"l5[:]   :{l5[:]}")


# slicing in reverse
print("-" * 40)
print(f"l5[-1] :{l5[-1]}")
print(f"l5[-1:-6:-1] :{l5[-1:-6:-1]}")
print(f"l5[-6:-11:-1] :{l5[-6:-11:-1]}")
print(f"l5[-1:-11:-1] :{l5[-1:-11:-1]}")
print(f"l5[-1::-1] :{l5[-1::-1]}")
print(f"l5[:-11:-1] :{l5[:-11:-1]}")
print(f"l5[::-1] :{l5[::-1]}")

# print(l5[10])

print("-" * 40)
l = [1, 2, 3, 4, 5]
print(f"l :{l}")

l[3] = 100
del l[1]
print(f"l :{l}")

# l[5] = "hello"
# print(f"l[5] :{l[5]}")
print("-" * 40)
print(dir(l))
