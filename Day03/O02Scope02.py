
# global

glbX = 100

def greet(name):
    global glbX                         # do not assign any value
    glbX = 500
    gname = f"Mr. {name}"
    print(f"Greeting {gname}")
    print(f"glbX Inside :{glbX}")


print(f"glbX Before :{glbX}")

greet("Sachin")

print(f"glbX After :{glbX}")

