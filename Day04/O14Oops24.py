
class HDFC:

    def withDraw(self, amt):
        print("You can with draw upto 2.5 lakhs per day")

# __name__ in the current program is the name of the current module
print("Module :", __name__)

if __name__ == '__main__':
    hdfc = HDFC()
    hdfc.withDraw(5000)
