
FL = open("EMP.csv", "r")

gen = {}
desig = []
dept = []
sal = 0

for line in FL.readlines():
    # print(line, end="")
    g = line.split(",")[2]
    ds = line.split(",")[3]
    dp = line.split(",")[4]
    if g not in gen:
        gen[g] = 1
    else:
        gen[g] += 1

    if dp not in dept:
        dept.append(dp)

    if ds not in desig:
        desig.append(ds)

    sal += int(line.split(",")[5])

FL.close()

print(f"Gender :{gen}")
print(f"Desin :{desig}")
print(f"Department :{dept}")
print(f"Sum of all Salaries :{sal}")
