
print("update".center(40, "-"))

emp1 = {'name': 'John', 'age': 36, 'desig': 'MGR', 'dept': "Finanace"}
emp2 = {'name': 'Tina', 'age': 32, 'desig': 'TL', 'sal': 70000}

print(f"emp1 :{emp1}")
print(f"emp2 :{emp2}")

emp1.update(emp2)
print("-" * 40)
print(f"emp1 After :{emp1}")

print("copy".center(40, "-"))

emp1= {'name': 'John', 'age': 36, 'desig': 'MGR', 'dept': "Finanace", 'sal': 85000}
print(f"emp1 Before :{emp1}")
emp2 = emp1
print(f"emp2 Before :{emp2}")

print("-" * 40)
emp2['gender'] = 'female'
print(f"emp2 After :{emp2}")
print(f"emp1 After :{emp1}")

print("-" * 40)

emp1= {'name': 'John', 'age': 36, 'desig': 'MGR', 'dept': "Finanace", 'sal': 85000}
print(f"emp1 Before :{emp1}")
emp2 = emp1.copy()
print(f"emp2 Before :{emp2}")

print("-" * 40)
emp2['gender'] = 'male'
print(f"emp2 After :{emp2}")
print(f"emp1 After :{emp1}")

print("-" * 40)

emp1 = {'name': 'John', 'age': 36, 'desig': 'MGR',
'dept': ['accounts', 'Finanace', 'HR'],
'marks': {'Degree': '89%','PG': '93%'}}

print(f"emp1 Before :{emp1}")
emp2 = emp1.copy()
print(f"emp2 Before :{emp2}")

print("-" * 40)

emp2['dept'].append('Management')
emp2['marks']['Xth'] = '83%'

print(f"emp2 After :{emp2}")
print(f"emp1 After :{emp1}")

print("-" * 40)

emp1 = {'name': 'John', 'age': 36, 'desig': 'MGR',
'dept': ['accounts', 'Finanace', 'HR'],
'marks': {'Degree': '89%','PG': '93%'}}

from copy import deepcopy

print(f"emp1 Before :{emp1}")
emp2 = deepcopy(emp1)
print(f"emp2 Before :{emp2}")

print("-" * 40)

emp2['dept'].append('Management')
emp2['marks']['Xth'] = '83%'

print(f"emp2 After :{emp2}")
print(f"emp1 After :{emp1}")
