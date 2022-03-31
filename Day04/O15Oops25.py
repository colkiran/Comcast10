
import O14Oops24

def withDraw(self):
    print("You can withdraw upto 4k per day......")

O14Oops24.HDFC.withDraw = withDraw              # monkey patching

hdfc = O14Oops24.HDFC()
hdfc.withDraw()

