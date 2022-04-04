
import pickle

PFR = open("PlayersPickle", "rb")                   # rb - read and binary

plyr = pickle.load(PFR)

for k, info in plyr.items():
    print(k)
    print("----")
    for ky, vl in info.items():
        print(ky, "=>", vl)
    print("-" * 40)
