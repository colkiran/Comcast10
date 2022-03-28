
print("items".center(40, "-"))
# items is a combination of keys and values function

emp = {
    'emp1': {'name': 'John', 'age': 36, 'desig': 'MGR', 'dept': "Finanace", 'sal': 85000},
    'emp2': {'name': 'Tina', 'age': 32, 'desig': 'TL', 'dept': 'HR', 'sal': 70000},
    'emp3': {'name': 'Kevin', 'age': 38, 'desig': 'Ana', 'dept': 'IT', 'sal': 125000}
}

print(f"emp :{emp}")

print("-" * 40)
print(f"emp['emp1'] :{emp['emp1']}")
print(f"emp['emp2'] :{emp['emp2']}")
print(f"emp['emp3'] :{emp['emp3']}")

for ky, info in emp.items():
    print(ky)
    print("------")
    for k, v in info.items():
        print(k, "=>", v)
    print("-" * 40)

