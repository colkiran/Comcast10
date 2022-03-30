
def outerFun(name):
    gname = f"Mr. {name}"

    def innerFun():

        print(f"Hello {gname}")

    return innerFun                     # HOF - Higher Order Function


outerFun("Sachin")()            # call the innerFun
print("-"* 40)

print(outerFun.__name__)            # __name__ => double underscore => dunder name
print(outerFun("Rohit").__name__)

print("-"* 40)
innerRef = outerFun("Virat")
innerRef()