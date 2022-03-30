
def outerFun(greet):
    def innerFun(sep):
        def innerMostFun(gname):
            import emojis
            emojized = emojis.encode(greet + " :" + sep + ": " + gname)
            print(emojized)
        return innerMostFun
    return innerFun

engGrt = outerFun("Welcome")

tigerimg = engGrt("tiger")
lionimg = engGrt("lion")
elepimg = engGrt("elephant")

tigerimg("Sheroff")
lionimg("Mike Tyson")
elepimg("Tony")


"""

outerFun("Welcome")("---->")("Sachin")
print("-" *  40)

engGrt = outerFun("Welcome")
tamilGrt = outerFun("Vanakam")

Esglln = engGrt("----->")
Tsglln = tamilGrt("----->")
Edbln = engGrt("=====>")
Tdbln = tamilGrt("=====>")

Edbln("Sehwag")
Tsglln("Ashwin")

"""