
import sys
for path in sys.path:
    print(path)

print("=" * 40)
from gurgaon.mymodule import Player

ply1 = Player("Kapil Dev", 67)
ply1.get_details()
