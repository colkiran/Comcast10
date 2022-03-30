
def outerFun(name):
    gname = f"Mr. {name}"

    def innerFun():

        print(f"Hello {gname}")

    innerFun()


outerFun("Sachin")