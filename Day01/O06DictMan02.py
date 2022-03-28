
"""
'clear', 'copy', 'fromkeys', 'get', 'items', 'keys',
'pop', 'popitem', 'setdefault', 'update', 'values'
"""
print("keys".center(40, "-"))
player = {'name': 'sachin', 'runs': 85, 'oppn': 'WI', 'venue': 'sabina park', 'year': 2003}
print(f"player :{player}")

k = player.keys()
print(f"k :{k}")

for i in k:
    print(i, end=" ")
print()
print("-" * 40)

for k in player.keys():
    print(k + " => " + str(player[k]))

print("values".center(40, "-"))
player = {'name': 'sachin', 'runs': 85, 'oppn': 'WI', 'venue': 'sabina park', 'year': 2003}
print(f"player :{player}")

v = player.values()
print(f"v :{v}")
for i in v:
    print(i, end=" ")
print()

print("fromkeys".center(40, "-"))
cities = ['blr', 'che', 'mum', 'hyd', 'kol', 'del']
print(f"cities :{cities}")

# convert these cities into dictionary keys
res = dict.fromkeys(cities)
print(f"res :{res}")

res1 = dict.fromkeys(cities,24)
print(f"res :{res1}")

print("setdefault".center(40, "-"))
# used to add new key value pairs into the dictionary
player = {'name': 'sachin', 'runs': 85, 'oppn': 'WI', 'venue': 'sabina park', 'year': 2003}
print(f"player :{player}")

player.setdefault("oppn", "AUS")                # modify a key which is already present
player.setdefault('age', 34)                    # add a new key value pair
print(f"player :{player}")

print("pop".center(40, "-"))
player = {'name': 'sachin', 'runs': 85, 'oppn': 'WI', 'venue': 'sabina park', 'year': 2003}
print(f"player :{player}")

res = player.pop('year')
print(f"res :{res}")
print(f"player :{player}")

print("popitem".center(40, "-"))
player = {'name': 'sachin', 'runs': 85, 'oppn': 'WI', 'venue': 'sabina park', 'year': 2003}
print(f"player :{player}")

res = player.popitem()
print(f"res :{res}")
print(f"player :{player}")


