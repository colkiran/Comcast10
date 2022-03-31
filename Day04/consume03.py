
import sys

sys.path.append("c:/delhi")

for path in sys.path:
    print(path)

print("=" * 40)

from gurgaon.mymodule import Player

ply1 = Player("Mike Tyson", 38)

ply1.get_details()

