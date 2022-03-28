
d1 = dict()
print(f"d1 :{d1}")
print(type(d1))

print("-" * 40)
d2 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(f"d2 :{d2}")
print(type(d2))

print("-" * 40)
d3 = dict([('name', 'sachin'), ('runs', 85), ('oppn', 'WI'), ('venue', 'sabina park'), ('year', 2003)])
print(f"d3 :{d3}")
print(type(d3))

print("-" * 40)
d4 = dict(name="Rahul", runs=135, oppn='sri lanka', venue='chepauk', year=2005)
print(f"d4 :{d4}")
print(type(d4))

print("-" * 40)
player = {'name': 'sachin', 'runs': 85, 'oppn': 'WI', 'venue': 'sabina park', 'year': 2003}
print(f"player :{player}")
print(player['name'])
print(player['venue'])

player['venue'] = 'kensington'              # modify the existing key with the new value
player['age'] = 35                          # add a new key value pair into the dictionary
del player['year']                          # delete the key and the value is lost
print(f"player :{player}")

print("-" * 40)
# print(f"player['year'] :{player['year']}")
print(f"player.get('year') :{player.get('year')}")
print(f"player.get('year') :{player.get('year', 'Not a valid Key, Please mention the correct one....')}")
print(f"player.get('name') :{player.get('name')}")

print("-" * 40)
print(dir(player))
