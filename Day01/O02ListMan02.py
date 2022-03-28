
"""
'append', 'clear', 'copy', 'count', 'extend', 'index',
 'insert', 'pop', 'remove', 'reverse', 'sort'

"""
print("append".center(40, "-"))
l1 = list(range(1, 6))
print(f"l1 :{l1}")
l1.append(6)
l1.append(7)
l1.append(8)

l1.append([9, 10, 11, 12, 13])
print(f"l1 :{l1}")
print(f"l1[8] :{l1[8]}")
print(f"l1[8][1:4] :{l1[8][1:4]}")


print("Extend".center(40, "-"))
l2 = [5, 6, 7, 8, 9, 10]
print(f"l2 :{l2}")
l2.extend([11, 12, 13, 14, 15])
print(f"l2 :{l2}")

print("Insert".center(40, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")
l1.insert(1, 1.5)
l1.insert(3, 2.5)
l1.insert(5, 3.5)
l1.insert(7, 4.5)
print(f"l1 :{l1}")

# pop, remove
print("pop".center(40, "-"))
l1 = list(range(1, 11))
print(f"l1 :{l1}")

res = l1.pop(4)
print(f"res :{res}")
print(f"l1 :{l1}")

res = l1.pop()                  # removes the last element of the list if the index is not specified
print(f"res :{res}")
print(f"l1 :{l1}")

res = l1.pop()
print(f"res :{res}")
print(f"l1 :{l1}")

print("remove".center(40, "-"))
l1 = [1, 2, 1 ,3, 1, 1, 2, 1, 2, 3, 1, 1, 2, 2, 1, 4, 3, 1, 2, 1, 1, 1, 1, 1]
print(f"l1 :{l1}")
res = l1.remove(1)
print(f"res :{res}")
print(f"l1 :{l1}")

while True:
    try:
        l1.remove(1)
    except ValueError:
        break

print(f"l1 :{l1}")