"""
nested functions
----------------
outerFun is the parent of innerFun
variable declared in the outerFun can be printed in the innerFun
but cannot be maniputlated unless we use a scope called nonlocal
"""

def outerFun(name):                 # local variable
    gname = f"Mr. {name}"           # local variable

    def innerFun():
        nonlocal gname
        gname += " Tendulkar"
        print(f"Hello {gname}.....")

    innerFun()
    print(f"gname After :{gname}")

outerFun("Sachin")