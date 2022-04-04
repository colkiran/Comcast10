
import pickle

ply1 = {'name': "Sachin Tendulkar", 'runs': 128, 'oppn': 'AUS', 'venue': 'Perth', 'year': 2005}
ply2 = {'name': "Sourav Ganguly", 'runs': 145, 'oppn': 'PAK', 'venue': 'Sharjah', 'year': 2002}

print(f"ply1 :{ply1}")
print(f"ply2 :{ply2}")
players = {}
players['p1'] = ply1
players['p2'] = ply2

FP = open("PlayersPickle", "ab")                 # ab - append and binary
pickle.dump(players, FP)
FP.close()
