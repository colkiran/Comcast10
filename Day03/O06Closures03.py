
def outerFun(greet):
    def innerFun(gname):
        print(greet, gname)

    return innerFun

outerFun("Welcome")("Sachin")
print("-"* 40)

# simple curry
engGrt = outerFun("Welcome")
spnGrt = outerFun("Hola")
tamilGrt = outerFun("Vanakam")

engGrt("Rahul")
spnGrt("Messi")
spnGrt("Nadal")
tamilGrt("Dhoni")

